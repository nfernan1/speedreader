from goody       import safe_open
import math
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    d = {}
    content = file.readlines()
    for line in content:
        l = line.strip()
        l = l.split(';')
        if l[0] not in d:
            d[l[0]] = set(l[1])
        else:
            d[l[0]].add(l[1])
        if l[1] not in d:
            d[l[1]] = set(l[0])
        else:
            d[l[1]].add(l[0])   
    return d

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes')
    for node in sorted(graph):
        print('\t{} -> {}'.format(node, graph[node]))

def find_influencers(graph):
    infl = {}
    s = set()
    for node in graph:
        temp_node = ((len(graph[node])) - (math.ceil(len(graph[node])/2)))
        infl[node] = temp_node
   
                


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
