import pytest

from pytest_csv_params.decorator import csv_params

@csv_params("tests/resources/examples.csv")
def test_statements(statement: str, schema: str, correct_query:str):
    print(schema)
    print(correct_query)
