from antlr4 import InputStream, CommonTokenStream
from tokenize import tokenize, OP
from io import BytesIO
from logging import debug, info
import operator
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

    def match(self, p: Pattern, op: operator) -> Result:
        assert p.types
        for type in p.types:
            for s in self.entries:
                if type==s.type:
                    if op(s.start in p.start, s.end in p.end):
                        return Result.MATCH
                    elif op(s.start in p.end, s.end in p.start):
                        return Result.REVERSE_MATCH        
        return Result.NO_MATCH  
    
    def match_unspecified_reltype(self, p: Pattern) -> Result:
        assert not p.types
        for s in self.entries:         
            if s.start in p.start and s.end in p.end:
                return Result.MATCH
            if s.start in p.end and s.end in p.start:
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
            if labels:
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
        if r.nodePattern():
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

def evaluate_relationship(r: Pattern, schema: Schema, query: str) -> str:
    if r.types:
        match schema.match(r, operator.__and__):
            case Result.MATCH:
                return query
            case Result.REVERSE_MATCH:
                return reversedQuery(r, query)
            case Result.NO_MATCH:
                if (r.start and r.end and r.start!=r.end):
                    return ""
                else: 
                    match schema.match(r, operator.__or__):
                        case Result.MATCH:
                            return query
                        case Result.REVERSE_MATCH:
                            return reversedQuery(r, query)
    else:
        match schema.match_unspecified_reltype(r):
            case Result.MATCH:
                return query
            case Result.REVERSE_MATCH:
                return reversedQuery(r, query)
    return query

def remove_line_breaks(s:str):
    return s.replace('\n', ' ').replace('\r',' ')
    
def fix_direction(query: str, schemaStr: str):
    relationships = extractRelationships(query)
    info(f"relationships {relationships}")
    schema = tokenizeSchema(schemaStr)
    info(f"schema {schema}")
    # evaluate the reversion/replacement rules
    for r in relationships:
        debug(f"{remove_line_breaks(query)} for {r} ")
        query = evaluate_relationship(r, schema, query)
        debug(f"{remove_line_breaks(query)} result")
            
    return query