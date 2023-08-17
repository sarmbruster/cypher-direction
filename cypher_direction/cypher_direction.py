from antlr4 import InputStream, CommonTokenStream
from tokenize import tokenize, OP
from io import BytesIO
from logging import debug, info, warning
import inspect, sys
from cypher_direction.CypherLexer import CypherLexer
from cypher_direction.CypherParser import CypherParser
from cypher_direction.Trees import Trees

def strip_or_none(s: str) -> str:
    return None if s is None else s.strip('`')

class Pattern:
    """contains normalized patterns from a cypher statement"""
    def __init__(self, start: str, types: list[str], end: str, startIndex: int, endIndex: int, text: str):
        self.start = strip_or_none(start)
        self.end = strip_or_none(end)
        self.types = types
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.text = text
        
    def __str__(self) -> str:
        return f"(:{self.start})-[:{'|'.join(self.types)}]->(:{self.end})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class SchemaPattern:
    """representation of schema entried"""
    def __init__(self, start: str, type: str, end: str):
        self.start = start
        self.end = end
        self.type = type
        
    def __str__(self) -> str:
        return f"(:{self.start})-[:self.type]->(:{self.end})"
    
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

def getRelationshipTypes(rel) -> list[str]:
    try:
        return sorted(map(lambda r: r.getText(), rel.labelExpression().labelExpression4().labelExpression3()))
    except AttributeError:
        return []
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
                types = getRelationshipTypes(rel)           
                relationships.append(Pattern(
                    startLabel if right is not None else endLabel, 
                    types,
                    endLabel if right is not None else startLabel,
                    rel.start.start,
                    rel.stop.stop,
                    rel.getText()
                ))
            startLabel = endLabel
    return relationships

def tokenizeSchema(schema: str) -> list[SchemaPattern]:
    schemaDefinitions = []
    i = iter(tokenize(BytesIO(schema.encode('utf-8')).readline))
    while (x := next(i, None)) is not None:
        if x.type == OP and x.string == '(':
            startLabel = next(i).string
            next(i) # comma
            relType = next(i).string
            next(i) # comma
            endLabel = next(i).string
            schemaDefinitions.append(SchemaPattern(startLabel, relType, endLabel))
    return schemaDefinitions

def exactlyOne(iterator):
    if next(iterator, None) is None:
        return False
    elif next(iterator, None) is None:
            return True
    return False

def matches_both_abels_reltype(r: Pattern, schemaDefinitions: list[Pattern]) -> bool:
    return all(filter(lambda t: any(filter(lambda s: r.start == s.start and r.end == s.end and r.types==s.types, schemaDefinitions)), r.types))
   # return any(filter(lambda s: r.start == s.start and r.end == s.end and r.types==s.types, schemaDefinitions))

def matches_both_abels_reltype_opposite_direction(r: Pattern, schemaDefinitions: list[Pattern]) -> bool:
    return all(filter(lambda t: any(filter(lambda s: r.start == s.end and r.end == s.start and r.types==s.types, schemaDefinitions)), r.types))
    #return any(filter(lambda s: r.start == s.end and r.end == s.start and r.types==s.types, schemaDefinitions))

def matches_exactly_one_entry_both_labels_empty_reltype(r: Pattern, schemaDefinitions: list[Pattern]) -> bool:
    return exactlyOne(filter(lambda s: r.start == s.end and r.end == s.start and len(r.types)==0, schemaDefinitions))

def matches_onelabel_and_reltype(r: Pattern, schemaDefinitions: list[Pattern]) -> bool:
    return exactlyOne(filter(lambda s: (r.start is None or r.start == s.end) and (r.end is None or r.end == s.start) and r.types==s.types, schemaDefinitions))



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
    
def reversedQuery(p: Pattern, query: str) -> str :
    reversedPattern = reverse(p.text)
    return f"{query[:p.startIndex]}{reversedPattern}{query[p.endIndex+1:]}"

def rule00(r: Pattern, schemaDefinitions: list[SchemaPattern], query: str) -> (bool, str):
    """if we find a full match, skip processing. If there's a full reversed match, reverse the query pattern"""
    if all(
        map(lambda t : any(
            filter(lambda s: t==s.type and r.start==s.start and r.end==s.end, schemaDefinitions)
        ), r.types)
    ):
        return (True, query)
    elif all(
        map(lambda t : any(
            filter(lambda s: t==s.type and r.start==s.end and r.end==s.start, schemaDefinitions)
        ), r.types)
    ):
        return (True, reversedQuery(r, query))
    else:
        return (False, query)

def rule01(r: Pattern, schemaDefinitions: list[SchemaPattern], query: str) -> (bool, str):
    """If the given pattern in a Cypher statement doesn't fit the graph schema, simply return an empty string"""
    if any(filter(
        lambda x: 
            any(filter(
                lambda y:  x==y.type and ((r.start==y.start and r.end==y.end) or (r.start==y.end and r.end==y.start)), 
            schemaDefinitions)), 
        r.types)):
        return (False, query)
    else:
        return (True, '') 
    
def rule02(r: Pattern, schemaDefinitions: list[SchemaPattern], query: str) -> (bool, str):
    """If the relationship is between two nodes of the same labels, there is nothing to validate or correct"""
    if r.start == r.end:
        return (True, query)
    else:
        return (False, query)
    
def rule03(r: Pattern, schemaDefinitions: list[SchemaPattern], query: str) -> (bool, str):
    """If the input query has an undirected relationship in the pattern, we do not correct it."""
    # undirected rels are not listed, so continue
    return (False, query)

def rule04(r: Pattern, schemaDefinitions: list[SchemaPattern], query: str) -> (bool, str):
    """If a node label is missing in the defined pattern, we can still validate if it fits the graph schema"""
    if r.start is None or r.end is None:
        if len(r.types) != 1:
            raise "tmp"
        if any(filter(lambda x: r.types[0] == x.type and (r.start is None or r.start==x.end) and (r.end is None or r.end==x.start), schemaDefinitions)):
            return (True, reversedQuery(r, query))
        else:
            return (False, query) 
    return (False, query)

def rule05(r: Pattern, schemaDefinitions: list[SchemaPattern], query: str) -> (bool, str):
    """If the input query doesn't define the relaitionship type, but at least one node label is given of a pattern, 
    we check if any relationship exists that matches the pattern and correct it if needed"""
    return (False, query)
    
def getRulesFunctions():
    return sorted([obj for name,obj in inspect.getmembers(sys.modules[__name__]) 
        if (inspect.isfunction(obj) and name.startswith('rule') )], key=lambda x: x.__name__)
    
def fix_direction(query: str, schema: str):
    relationships = extractRelationships(query)
    info(f"relationships {relationships}")
    schemaDefinitions = tokenizeSchema(schema)
    info(f"schema {schemaDefinitions}")
    rules = getRulesFunctions()
    # evaluate the reversion/replacement rules
    for r in relationships:

        
        for rule in rules:
            debug(f"{rule.__name__} : {query} for {r} ")
            (doBreak, query) = rule(r, schemaDefinitions, query)
            debug(f"{rule.__name__} : {query} result break {doBreak}")
            if doBreak:
                break
            
    return query