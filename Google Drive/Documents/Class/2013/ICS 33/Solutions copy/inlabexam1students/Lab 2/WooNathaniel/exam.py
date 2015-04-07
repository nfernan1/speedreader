from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    lines = [line for line in file.readlines()]
    nodelines = [node.strip('\n') for node in lines]
    nodes = [tuple(item.split(';')) for item in nodelines]
    d = defaultdict(set)
    for k,v in nodes:
        d[k].add(v)
        d[v].add(k)
    return d

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for item in sorted(graph):
        print('{} -> {} '.format(item,sorted(graph[item])))
        

def find_influencers(graph):
    infl = {}
    while True:
        for key in graph:
            infl[key] = len(graph[key])- ceil(0.5*len(graph[key]))
        cand = [(infl[key],len(graph[key]),key) for key in infl.keys() if infl[key] >= 0]
        vals = [item[0] for item in cand]
        cand.pop(vals.index(min(vals)))
        print(cand)
        if len(cand) == 0:
            return infl

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))