# Derick Nguyen 91841700 Lab 3

from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        x,y = line.strip().split(';')
        graph[x].add(y)
        graph[y].add(x)
    return graph

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for x,y in sorted(graph.items()):
        print(' ',x, '->', sorted(y)) 
    
def find_influencers(graph):
    influ = defaultdict()
    for x,y in sorted(graph.items()):
        influ[x] = len(y) - (ceil(len(y)/2))
    cand = []
    for key in influ.keys():
        if influ[key] >= 0: 
            x = tuple((influ[key], len(graph[key]), key))             
            cand.append(x)
    while len(cand) > 0:
        cand = sorted(cand)
        k = sorted(cand).pop([0])
        for each in influ[k]:
            influ[each] = influ[each] - 1
            print(influ)
    return set(influ.keys())

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
