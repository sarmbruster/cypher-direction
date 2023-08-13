import pycypher

def fix_direction(query: str, schema: str):
    parsed = pycypher.parse(query)
    return query