from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    result = defaultdict(set)
    keys = []
    for line in file.readlines():
        keys.append(line.strip().split(';'))
    for tuple in keys:
        for letter in tuple:
            result[letter]
        if tuple[0] in result.keys():
            result[tuple[0]].add(tuple[1])
            
    print(result)
    return result

    
def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    nodes = graph.items()
    for node in sorted(nodes):
        print('{} -> {}'.format(node[0], node[1]))


def find_influencers(graph):
    infl = defaultdict(int)
    cand = []
    for key in graph.keys():
        value = ceil(len(graph[key])/2)
        infl[key] += value
        for k in infl.keys():
            cand.append((infl[k], graph[k], k))
    print(cand)
    while cand:
        min_tuple = min(cand)
        cand.pop(min_tuple)
        for value in infl():
            if min_tuple[2] in infl[value].values():
                infl[min_tuple[2]] -= 1
    
    
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
