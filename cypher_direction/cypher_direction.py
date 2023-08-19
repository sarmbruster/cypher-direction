from antlr4 import InputStream, CommonTokenStream
from tokenize import tokenize, OP
from io import BytesIO
from logging import debug, info
import inspect, sys
from enum import Enum
from cypher_direction.CypherLexer import CypherLexer
from cypher_direction.CypherParser import CypherParser
from cypher_direction.Trees import Trees

def strip_or_none(s: str) -> str:
    return None if s is None else s.strip('`')

class Result(Enum):
    MATCH = 1
    REVERSE_MATCH = 2
    NO_MATCH = 3

class SchemaPattern:
    """representation of schema entry"""
    def __init__(self, start: str, type: str, end: str):
        self.start = start
        self.end = end
        self.type = type
        
    def __str__(self) -> str:
        return f"(:{self.start})-[:{self.type}]->(:{self.end})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Pattern:
    """contains normalized patterns from a cypher statement"""
    def __init__(self, start: [str], types: list[str], end: [str], startIndex: int, endIndex: int, text: str):
        self.start = start
        self.end = end
        self.types = types
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.text = text
        
    def __str__(self) -> str:
        return f"(:{':'.join(self.start)})-[:{'|'.join(self.types)}]->(:{':'.join(self.end)})"
    
    def __repr__(self) -> str:
        return self.__str__()
        
class Schema:
    """representation of schema"""
    def __init__(self):
        self.entries = []

    def add(self, start: str, type: str, end: str):
        self.entries.append(SchemaPattern(start, type, end))

    def for_reltype(self, reltype: str):
        return filter(lambda x: x.type==reltype, self.entries)
    
    def match(self, p: Pattern) -> Result:
        for type in p.types:
            for s in self.entries:
                if type==s.type:
                    if any(filter(lambda x: x==s.start,p.start)) and any(filter(lambda x: x==s.end, p.end)):
                    #(p.start is None or p.start == s.start) and (p.end is None or p.end == s.end):
                        return Result.MATCH
                    elif any(filter(lambda x: x==s.end,p.start)) and any(filter(lambda x: x==s.start, p.end)):
                    #elif (p.start is None or p.start == s.end) and (p.end is None or p.end == s.start):
                        return Result.REVERSE_MATCH        
        return Result.NO_MATCH  
    
    def match_one_side(self, p: Pattern) -> Result:
        for type in p.types:
            for s in self.entries:
                if type==s.type:
                    if any(filter(lambda x: x==s.start,p.start)) or any(filter(lambda x: x==s.end, p.end)):
                        return Result.MATCH
                    if any(filter(lambda x: x==s.end,p.start)) or any(filter(lambda x: x==s.start, p.end)):
                        return Result.REVERSE_MATCH
        return Result.NO_MATCH  
    
    def match_unspecified_reltype(self, p: Pattern) -> Result:
        assert not p.types
        for s in self.entries:         
            if any(filter(lambda x: x==s.start,p.start)) and any(filter(lambda x: x==s.end, p.end)):
                return Result.MATCH
            if any(filter(lambda x: x==s.end,p.start)) and any(filter(lambda x: x==s.start, p.end)):
                return Result.REVERSE_MATCH       
        return Result.NO_MATCH  
    
    def __str__(self) -> str:
        return f"schema: {self.entries}"
    
    def __repr__(self) -> str:
        return self.__str__()
    

def getSymbolicName(nodePattern) -> str:
    try:
        return nodePattern.variable().symbolicNameString().unescapedSymbolicNameString().getText()
    except AttributeError:
        return None
    
def getLabels(nodePattern, namedNodes: {}) -> str:
        nodeLabels = nodePattern.labelExpression()
        if nodeLabels is None:
            symbolicName = getSymbolicName(nodePattern)
            return namedNodes.get(symbolicName, [])
        else:
            labels3 = nodeLabels.labelExpression4().labelExpression3()
            if len(labels3)>1:
                raise "more than one label"
            labels2 = labels3[0].labelExpression2()
            return list(map(lambda x: strip_or_none(x.getText()), labels2))

def fetchNamedNodes(tree) -> {}:
    result = {}
    for n in Trees.findAllRuleNodes(tree, CypherParser.RULE_nodePattern):
        symbolicName = getSymbolicName(n)
        if symbolicName is not None:
            labels = getLabels(n, {})
            if len(labels) > 0:
                result[symbolicName] = labels
    return result

def getRelationshipTypes(rel) -> list[str]:
    try:
        return sorted(map(lambda r: strip_or_none(r.getText()).strip('!'), rel.labelExpression().labelExpression4().labelExpression3()))
    except AttributeError:
        return []

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
        if len(r.nodePattern())>0:
            children = r.getChildren()
            startLabels = getLabels(next(children), namedNodes)

            while ((rel := next(children, None)) is not None):
                if isinstance(rel, CypherParser.MaybeQuantifiedRelationshipPatternContext):
                    rel = rel.relationshipPattern()
                left = rel.leftArrow()
                right = rel.rightArrow()
                endLabels = getLabels(next(children), namedNodes)
                if left is not None or right is not None:  # we don't care if direction is undefined
                    types = getRelationshipTypes(rel)    
                    text = rel.getText().replace('{',' {')       
                    relationships.append(Pattern(
                        startLabels if right is not None else endLabels, 
                        types,
                        endLabels if right is not None else startLabels,
                        rel.start.start,
                        rel.stop.stop,
                        text
                    ))
                startLabels = endLabels
    return relationships

def tokenizeSchema(schemaStr: str) -> list[SchemaPattern]:
    schema = Schema()
    i = iter(tokenize(BytesIO(schemaStr.encode('utf-8')).readline))
    while (x := next(i, None)) is not None:
        if x.type == OP and x.string == '(':
            startLabel = next(i).string
            next(i) # comma
            relType = next(i).string
            next(i) # comma
            endLabel = next(i).string
            schema.add(startLabel, relType, endLabel)
    return schema

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

def rule01(r: Pattern, schema: Schema, query: str) -> (bool, str):
    """if we find a full match, skip processing. If there's a full reversed match, reverse the query pattern"""
    if r.types:
        match schema.match(r):
            case Result.MATCH:
                return (True, query)
            case Result.REVERSE_MATCH:
                return (True, reversedQuery(r, query))
            case Result.NO_MATCH:
                if (r.start and r.end and r.start!=r.end):
                    return (True, "")
    return (False, query)

def rule02(r: Pattern, schema: Schema, query: str) -> (bool, str):
    """If the input query doesn't define the relaitionship type, but at least one node label is given of a pattern, 
    we check if any relationship exists that matches the pattern and correct it if needed"""
    if not r.types and (r.start or r.end):
        match schema.match_unspecified_reltype(r):
            case Result.MATCH:
                return (True, query)
            case Result.REVERSE_MATCH:
                return (True, reversedQuery(r, query))

    return (False, query)

def rule03(r: Pattern, schema: Schema, query: str) -> (bool, str):
    """partial match on one label"""
    if r.types:
        match schema.match_one_side(r):
            case Result.MATCH:
                return (True, query)
            case Result.REVERSE_MATCH:
                return (True, reversedQuery(r, query))
    return (False, query)
    
def getRulesFunctions():
    return sorted([obj for name,obj in inspect.getmembers(sys.modules[__name__]) 
        if (inspect.isfunction(obj) and name.startswith('rule') )], key=lambda x: x.__name__)

def remove_line_breaks(s:str):
    return s.replace('\n', ' ').replace('\r',' ')
    
def fix_direction(query: str, schemaStr: str):
    relationships = extractRelationships(query)
    info(f"relationships {relationships}")
    schema = tokenizeSchema(schemaStr)
    info(f"schema {schema}")
    rules = getRulesFunctions()
    # evaluate the reversion/replacement rules
    for r in relationships:
        for rule in rules:
            debug(f"{rule.__name__} : {remove_line_breaks(query)} for {r} ")
            (doBreak, query) = rule(r, schema, query)
            debug(f"{rule.__name__} : {remove_line_breaks(query)} result break {doBreak}")
            if doBreak:
                break
            
    return query