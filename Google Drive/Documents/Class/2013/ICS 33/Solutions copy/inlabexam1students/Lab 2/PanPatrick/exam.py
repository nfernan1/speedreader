from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for i in file:
        j = i.strip().split(';')
        graph[j[0]].add(j[1])
        graph[j[1]].add(j[0])
    return dict(graph)

def print_graph(graph):
    k = list(graph)
    k.sort()
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for i in k:
        d = list(graph[i])
        d.sort()
        print(' ',i,'->',d)

def find_influencers(graph):
    infl = {}
    for i in graph:
        infl[i] = ceil(len(graph[i])/2)
    while True:
        cand = []
        for i in infl:
            if infl[i] > -1:
                cand.append((infl[i],len(graph[i]),i))



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))