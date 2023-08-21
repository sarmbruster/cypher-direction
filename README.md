# cypher-directions

This repo contains a contribution to the [Cypher direction competition](https://github.com/tomasonjo/cypher-direction-competition).
The competition's page describes well the motivation and requirements, therefore this page only focusses on my approach to it.

## general solution idea

### ANTLR

Neo4j does provide the Cypher grammer in the form of an [ANTLR G4](https://github.com/antlr/antlr4/blob/master/doc/grammars.md) file in their public repository at:

* <https://github.com/neo4j/neo4j/blob/5.10/community/cypher/front-end/antlr-parser/src/main/antlr4/org/neo4j/cypher/internal/parser/CypherParser.g4> and
* <https://github.com/neo4j/neo4j/blob/5.10/community/cypher/front-end/antlr-parser/src/main/antlr4/org/neo4j/cypher/internal/parser/CypherLexer.g4>

> **Warning**
> Originally I've tried to use the G4 file supplied by [openCypher](https://opencypher.org/resources/). During first tests it became clear that this grammer file does not reflect the current state of Cypher using in Neo4j 5.10.x. As an example openCypher's grammer file does not support subqueries `CALL { <subquery> }`.

[Antlr](https://www.antlr.org/) 4.13.0 is used to generate python code from the grammer file:

```sh
java -jar antlr-4.13.0-complete.jar -o cypher_direction -Dlanguage=Python3 CypherLexer.g4 CypherParser.g4
```

For simplicity the generation itself is not part of the project, instead the resulting files

* [cypher_direction/CypherParser.py](cypher_direction/CypherParser.py)
* [cypher_direction/CypherLexer.py](cypher_direction/CypherLexer.py)
* [cypher_direction/CypherListener.py](cypher_direction/CypherListener.py)
* [cypher_direction/CypherParserListener.py](cypher_direction/CypherParserListener.py)

habe been added to the repository.

### finding and evaluating relationship patterns

The provided schema string is parsed using Python's tokenize module.
The input query is parsed into an AST using the generated modules.
Relationship pattern are extracted from the AST by finding all `PathPatternAtom` and `PathPatternNonEmpty` elements and digest their subtrees.
For each relationship pattern a instance of `Pattern` is populated.
Those contain start and end labels, relationship types and start/end indexes of the location of the pattern in the originating string.

The patterns are now matched against the parsed schema information.
If a pattern is considered valid nothing happens.
if the pattern is reversed compared to the schema the relevant snippet of the original query is reversed.
In case the pattern does not match the schema at all and error is indicated by returning an empty string.

### testing

The code uses [pytest](https://pytest.org/) with the [pytest-csv-params](https://docs.codebau.dev/pytest-plugins/pytest-csv-params/) module to perform automated testing of all the [examples provided](tests/resources/examples.csv) for validation.

## building and running

The project uses poetry, therefore use

```sh
poetry install 
```

To run the tests:

```sh
pytest
```

Optionally `-v` can be amended for more verbose output.
