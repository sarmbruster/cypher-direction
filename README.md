# cypher-directions

This repo contains a contribution to the [Cypher direction competition](https://github.com/tomasonjo/cypher-direction-competition).
The competition's page describes well the motivation and requirements, therefore this page only focusses on my approach to it.

## general solution idea

Neo4j does provide the Cypher grammer in the form of an [ANTLR G4](https://github.com/antlr/antlr4/blob/master/doc/grammars.md) file in their public repository at:

* <https://github.com/neo4j/neo4j/blob/5.10/community/cypher/front-end/antlr-parser/src/main/antlr4/org/neo4j/cypher/internal/parser/CypherParser.g4> and
* <https://github.com/neo4j/neo4j/blob/5.10/community/cypher/front-end/antlr-parser/src/main/antlr4/org/neo4j/cypher/internal/parser/CypherLexer.g4>

> :warning: Originally I've tried to use the G4 file supplied by [openCypher](https://opencypher.org/resources/).
> During first tests it became clear that this grammer file does not reflect the current state of Cypher using in Neo4j 5.10.x.
> As an example openCypher's grammer file does not support subqueries `CALL { <subquery>}`.
