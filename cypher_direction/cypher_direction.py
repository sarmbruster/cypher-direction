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
        self.type = type.strip('`')
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.text = text
        
    def __str__(self) -> str:
        return f"(:{self.start})-[:{self.type}]->(:{self.end})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
def getLabel(nodePattern) -> str:
        labels = nodePattern.oC_NodeLabels().oC_NodeLabel()
        if len(labels)>1:
            raise "more than one label"
        label = labels[0].oC_LabelName().getText()
        return label

def extractRelationships(query: str) -> []:
    relationships = []
    input_stream = InputStream(query)
    lexer = CypherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CypherParser(stream)
    tree = parser.oC_Cypher()

    patternElements = Trees.findAllRuleNodes(tree, CypherParser.RULE_oC_PatternElement)
    for patternElement in patternElements:

        startLabel = getLabel(patternElement.oC_NodePattern())

        patternElementChain = patternElement.oC_PatternElementChain()
        for p in patternElementChain:
            rel = p.oC_RelationshipPattern()
            left = rel.oC_LeftArrowHead()
            right = rel.oC_RightArrowHead()
            if left is not None or right is not None:
                types = rel.oC_RelationshipDetail().oC_RelationshipTypes().oC_RelTypeName()
                if len(types) > 1:
                    raise "more than one relationship type"
                type = types[0].oC_SchemaName().getText()
                endLabel = getLabel(p.oC_NodePattern())

                relationships.append(Pattern(
                    startLabel if right is not None else endLabel, 
                    type,
                    endLabel if right is not None else startLabel,
                    rel.start.column,
                    rel.stop.column,
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
    return rel.start == schema.end and rel.end == schema.start and rel.type == schema.type

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