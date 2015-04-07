from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    i = file.readlines()
    for line in i:
        key,value = line.strip().split(';')
        graph[key].add(value)
        graph[value].add(key)
    return graph

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes(ordered)')
    for key, value in graph.items():
        #graph[key].sorted(graph.values())
        print(key, '->',value)

def find_influencers(graph):
    infl = {}
    cand = []
    for item in graph.keys():
        infl[item] = len(graph[item])-ceil((len(graph[item]))/2)
    for key in infl.keys():
        if infl[key] < 0:
            continue
        else:
            print(cand.append((len(graph[item])-ceil((len(graph[item]))/2), (len(graph[item])),key)))
    while True:
        small = tuple(cand)
        min = cand[0][0]
        for item in cand:
            if cand[0] < min:
                min = item[0]
                
    print('infl = ', infl)
    print('cand: ',cand)
    print("removing ", ,"as key from infl; decrementing friend's value")


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))