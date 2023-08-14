from antlr4 import InputStream, CommonTokenStream
from tokenize import tokenize, OP
from io import BytesIO
from cypher_direction.CypherLexer import CypherLexer
from cypher_direction.CypherParser import CypherParser
from cypher_direction.Trees import Trees

class Pattern:
    """contains normalized patterns from a cypher statement"""
    def __init__(self, start: str, type: str, end: str, startIndex: int, endIndex: int, text: str):
        self.start = start.strip('`')
        self.end = end.strip('`')
        self.type = type.strip('`') if type is not None else None
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.text = text
        
    def __str__(self) -> str:
        return f"(:{self.start})-[:{self.type}]->(:{self.end})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
def getLabel(nodePattern, namedNodes: {}) -> str:
        nodeLabels = nodePattern.oC_NodeLabels()
        if nodeLabels is None:
            symbolicName = nodePattern.oC_Variable().oC_SymbolicName().getText()
            return namedNodes.get(symbolicName, None) if namedNodes is not None else None
        else:
            labels = nodeLabels.oC_NodeLabel()
            if len(labels)>1:
                raise "more than one label"
            label = labels[0].oC_LabelName().getText()
            return label

def fetchNamedNodes(tree) -> {}:
    result = {}
    for n in Trees.findAllRuleNodes(tree, CypherParser.RULE_oC_NodePattern):
        variable = n.oC_Variable()
        if variable is not None:
            symbolicName = variable.oC_SymbolicName().getText()
            label = getLabel(n, None)
            if symbolicName is not None and label is not None:
                result[symbolicName]=label
    return result

def getRelationshipType(rel) -> str:
    relationshipDetail = rel.oC_RelationshipDetail()
    if relationshipDetail is None:
        return None
    else:
        types = relationshipDetail.oC_RelationshipTypes()
        if types is None:
            return None
        else:
            names = types.oC_RelTypeName()
            if len(names) > 1:
                raise "more than one relationship type"
            return names[0].oC_SchemaName().getText()

def extractRelationships(query: str) -> []:
    relationships = []
    input_stream = InputStream(query)
    lexer = CypherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CypherParser(stream)
    tree = parser.oC_Cypher()

    namedNodes = fetchNamedNodes(tree)

    elements = Trees.findAllRuleNodes(tree, CypherParser.RULE_oC_PatternElement)
    elements.extend(Trees.findAllRuleNodes(tree, CypherParser.RULE_oC_RelationshipsPattern))

    for r in elements:
        startLabel = getLabel(r.oC_NodePattern(), namedNodes)
        for p in r.oC_PatternElementChain():
            rel = p.oC_RelationshipPattern()
            left = rel.oC_LeftArrowHead()
            right = rel.oC_RightArrowHead()
            if left is not None or right is not None:  # we don't care if direction is undefined
                type = getRelationshipType(rel)           
                endLabel = getLabel(p.oC_NodePattern(), namedNodes)
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
        elif next(filter(lambda x: schemaMatchReverse(r,x), schemaDefinitions), None):
            print(f"{r} reversed found in schema {r.text}")
            reversedPattern = reverse(r.text)
            query = f"{query[:r.startIndex]}{reversedPattern}{query[r.endIndex+1:]}"
        else:
            raise(f"{r} not found in schema")
    return query