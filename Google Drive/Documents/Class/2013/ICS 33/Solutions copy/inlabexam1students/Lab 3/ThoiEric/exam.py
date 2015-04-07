from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    infile = open(file)
    nodes = infile.readlines()
    infile.close()
    map = []
    keys = set()
    d = dict()
    for i in nodes:
        map.append(i.strip('\n').split(';'))
    for i in map:
        keys.add(i[1])
        keys.add(i[0])
    for i in keys:
        d[i] = set()
    for i in map:
        d[i[0]].add(i[1])
        d[i[1]].add(i[0])
    return d    

def print_graph(graph):
    print('Graph: source nodes(ordered) -> destination nodes (ordered)')
    keys = list(graph.keys())
    keys.sort()
    for i in keys:
        print(i + ' -> ' + str(graph[i])) 
    

def find_influencers(graph):
    influ = dict()
    for i in graph:
        influ[i] = ceil(len(graph[i])/2)
    cand = []
    for i in influ:
        cand.append((influ[i], len(graph[i]), i))
    while len(cand) != 1:
        l = min(cand)
        cand.remove(l)
        for i in graph.keys():
            if l in graph[i]:
                for j in cand:
                    if j[2]==i:
                        j[0] -= 1
    return cand
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
