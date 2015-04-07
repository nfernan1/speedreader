from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    dict_graph = {}
    for x in file:
        dict_graph[x[0]] = set()
        dict_graph[x[2]] = set()
        for y in dict_graph.keys():
            if x[0] == y:
                dict_graph.get(y).update(x[2])
            elif x[2] == y:
                dict_graph.get(y).update(x[0])
    return dict_graph

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for x in sorted(graph):
        s = ', '.join(sorted(graph.get(x)))
        print('  {} -> {}'.format(x, s))
 
def find_influencers(graph):
    pass
 


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    #core = find_influencers(graph)
    #print('Influencers =', find_influencers(graph))
