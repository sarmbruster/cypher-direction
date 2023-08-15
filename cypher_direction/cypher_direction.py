from antlr4 import InputStream, CommonTokenStream
from tokenize import tokenize, OP
from io import BytesIO
from cypher_direction.CypherLexer import CypherLexer
from cypher_direction.CypherParser import CypherParser
from cypher_direction.Trees import Trees

def strip_or_none(s: str) -> str:
    return None if s is None else s.strip('`')

class Pattern:
    """contains normalized patterns from a cypher statement"""
    def __init__(self, start: str, type: str, end: str, startIndex: int, endIndex: int, text: str):
        self.start = strip_or_none(start)
        self.end = strip_or_none(end)
        self.type = strip_or_none(type)
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.text = text
        
    def __str__(self) -> str:
        return f"(:{self.start})-[:{self.type}]->(:{self.end})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
def getSymbolicName(nodePattern) -> str:
    try:
        return nodePattern.variable().symbolicNameString().unescapedSymbolicNameString().getText()
    except AttributeError:
        return None
    
def getLabel(nodePattern, namedNodes: {}) -> str:
        nodeLabels = nodePattern.labelExpression()
        if nodeLabels is None:
            symbolicName = getSymbolicName(nodePattern)
            return namedNodes.get(symbolicName, None) if namedNodes is not None else None
        else:
            labels3 = nodeLabels.labelExpression4().labelExpression3()
            if len(labels3)>1:
                raise "more than one label"
            labels2 = labels3[0].labelExpression2()
            if len(labels2) > 1:
                raise "more than one label"
            return strip_or_none(labels2[0].getText())

def fetchNamedNodes(tree) -> {}:
    result = {}
    for n in Trees.findAllRuleNodes(tree, CypherParser.RULE_nodePattern):
        symbolicName = getSymbolicName(n)
        if symbolicName is not None:
            label = getLabel(n, None)
            if label is not None:
                result[symbolicName] = label
    return result

def getRelationshipType(rel) -> str:
    return rel.labelExpression().labelExpression4().getText()
    # relationshipDetail = rel.oC_RelationshipDetail()
    # if relationshipDetail is None:
    #     return None
    # else:
    #     types = relationshipDetail.oC_RelationshipTypes()
    #     if types is None:
    #         return None
    #     else:
    #         names = types.oC_RelTypeName()
    #         if len(names) > 1:
    #             raise "more than one relationship type"
    #         return names[0].oC_SchemaName().getText()

def extractRelationships(query: str) -> []:
    relationships = []
    input_stream = InputStream(query)
    lexer = CypherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CypherParser(stream)
    tree = parser.statements()

    namedNodes = fetchNamedNodes(tree)

    elements = Trees.findAllRuleNodes(tree, CypherParser.RULE_pathPatternAtoms)
    elements.extend(Trees.findAllRuleNodes(tree, CypherParser.RULE_pathPatternNonEmpty))
    for r in elements:
        children = r.getChildren()
        startLabel = getLabel(next(children), namedNodes)

        while ((rel := next(children, None)) is not None):
            if isinstance(rel, CypherParser.MaybeQuantifiedRelationshipPatternContext):
                rel = rel.relationshipPattern()
            left = rel.leftArrow()
            right = rel.rightArrow()
            endLabel = getLabel(next(children), namedNodes)
            if left is not None or right is not None:  # we don't care if direction is undefined
                type = getRelationshipType(rel)           
                relationships.append(Pattern(
                    startLabel if right is not None else endLabel, 
                    type,
                    endLabel if right is not None else startLabel,
                    rel.start.start,
                    rel.stop.stop,
                    rel.getText()
                ))
            startLabel = endLabel
    return relationships

def tokenizeSchema(schema: str) -> []:
    schemaDefinitions = []
    i = iter(tokenize(BytesIO(schema.encode('utf-8')).readline))
    while (x := next(i, None)) is not None:
        if x.type == OP and x.string == '(':
            startLabel = next(i).string
            next(i) # comma
            relType = next(i).string
            next(i) # comma
            endLabel = next(i).string
            schemaDefinitions.append(Pattern(startLabel, relType, endLabel, 0, 0, None))
    return schemaDefinitions

def schemaMatch(rel: Pattern, schema: Pattern) -> bool:
    return rel.start == schema.start and rel.end == schema.end and rel.type == schema.type

def schemaMatchReverse(rel: Pattern, schema: Pattern) -> bool:
    return rel.start == schema.end and rel.end == schema.start and (rel.type == schema.type or rel.type is None)

def schemaMatchReversePartial(rel: Pattern, schema: Pattern) -> bool:
    return (rel.start is None or rel.start == schema.end) and (rel.end is None or rel.end == schema.start) and rel.type == schema.type

def reverse(text: str) -> str:
    """reverse the direction of a relationship pattern"""
    if text.startswith('<'):
        return f"{text[1:]}>"
    elif text.endswith('>'):
        return f"<{text[:-1]}"
    else:
        raise f"don't know how to deal with {str}"
    
def fix_direction(query: str, schema: str):
    relationships = extractRelationships(query)
    print(relationships)
    schemaDefinitions = tokenizeSchema(schema)
    
    for r in relationships:
        if next(filter(lambda x: schemaMatch(r, x), schemaDefinitions), None):
            print(f"{r} found in schema")
        elif next(filter(lambda x: schemaMatchReverse(r,x), schemaDefinitions), None) or next(filter(lambda x: schemaMatchReversePartial(r, x), schemaDefinitions), None):
            print(f"{r} reversed found in schema {r.text}")
            reversedPattern = reverse(r.text)
            query = f"{query[:r.startIndex]}{reversedPattern}{query[r.endIndex+1:]}"
        
        else:
            raise(f"{r} not found in schema")
    return query