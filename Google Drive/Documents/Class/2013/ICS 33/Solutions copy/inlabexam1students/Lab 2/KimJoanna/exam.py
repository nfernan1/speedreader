from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        graph[line[0]].add(line[2])
        graph[line[2]].add(line[0])
        if graph[line[0]] in graph.values():
            graph[line[0]].update(line[2])
    return graph


def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for i in sorted(graph):
        print('  {} -> {}'.format(i, graph[i]))
    

def find_influencers(graph):
    infl, cand = dict(), list()
    for i in sorted(graph):
        friends = (len(graph[i])-ceil(len(graph[i])/2))
        infl[i] = friends
    a = []
    for eachnum in graph:
        a.append(len(graph[eachnum]))
    for each, value, x in zip(infl.values(), infl.keys(), a):
        cand.append((each, x, value))
    while len(cand) > 0:
        amin = min(cand)
        cand.remove(amin)
        print()
        print('infl =', infl)
        print('cand =', cand)


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of fi le with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    print('Influencers =', find_influencers(graph))
