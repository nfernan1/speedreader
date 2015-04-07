from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = dict()
    for line in file.readlines():
        if line[0] in graph.keys():
            graph.update(line[0], set(line[2]))
            continue
        print(graph)
def print_graph(graph):
    key = graph.keys()
    value = graph.values()
    for key in graph:
        print(key, '->', value)
        

def find_influencers(graph):
    pass



# Script

if __name__ == '__main__':
    #graph = read_graph(safe_open('Enter name of file with graph', 'r',
    #                             'Could not find that file'))
    print_graph({'i':{'j'}, 'h':{'g'}, 'j':{'i','g'}, 'a':{'c','b'}, 'c':{'a','b','d','g'}, 'b':{'a','c'},'e':{'d'}, 'd':{'c','e','f'},'g':{'h','c','j'},'f':{'d'}})
    #core = find_influencers(graph)
    #print('Influencers =', find_influencers(graph))
