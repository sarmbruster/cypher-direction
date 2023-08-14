import pycypher


def traverse_node(tree, level:int, result):

    node = tree['node']

    print(f"{level}: type={node}") 
    if node['parent'] in ['PatternElementChain']:#'Pattern', 'PatternPart']:
        result.append(node)
        if node['text'].count('[:') > 1:
            print("HURZ")
    traverse_result(tree['children'], level+1, result)

def traverse_result(tree, level:int, result=[]):
    nodes = tree.get('result')
    if nodes:
        for n in nodes:
            traverse_node(n, level, result)
    else:
        print(f"{level}: leaf {tree}")
    return result

def fix_direction(query: str, schema: str):
    ast = pycypher.parse(query)

    result = traverse_result(ast, 0)
    #if len(result)>2:
    print(f"result={result}")
    return query