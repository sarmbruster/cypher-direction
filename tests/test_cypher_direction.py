import pytest
from cypher_direction import cypher_direction

from pytest_csv_params.decorator import csv_params

@csv_params("tests/resources/small.csv")
#@csv_params("tests/resources/examples.csv")
def test_statements(statement: str, schema: str, correct_query:str):
    assert correct_query == cypher_direction.fix_direction(statement, schema)
    #pytest.fail("HURZ")