from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        k,v = line.strip().split(';')
        graph[k].add(v)
        graph[v].add(k)
    return graph

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes(ordered)')
    for k,v in sorted(graph.items()):
        s = sorted(v)
        print('',k,'->',', '.join(s))

def find_influencers(graph):
    result = set()
    temp_dict = {}
    for k in graph:
        if math.ceil(len(temp_dict[k])/2) == 1:
            temp_dict[k] = graph[k]
            pass
    return result
            
    





# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
