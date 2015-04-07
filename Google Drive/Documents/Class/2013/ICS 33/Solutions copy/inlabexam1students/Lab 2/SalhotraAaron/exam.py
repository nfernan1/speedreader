from goody       import safe_open
from math        import ceil 
from collections import defaultdict
import math             
# Use dict or defaultdict


# Define your functions here.
#friend_dict = {'i': {'j'}}, 'h:':{'g'}, 'j':{'i', 'g'} 'a':{'c','b',}
#node = len(defaultdict)
 

def read_graph(file):
    file_name = open('graph.txt','r')
    graph = {}
    graph.add(file_name)
    return file_name

def print_graph(graph):
    graph = defaultdict
    graph.sort()
    print(graph)

graph = range(len(defaultdict))
influenced = 0

def find_influencers(graph):
    for i in graph:
        new_node = 0 
        for influenced in defaultdict:
            new_node += 1
            print(new_node)
        if new_node >= influenced:
            math.ceil(influenced/float(2))



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
