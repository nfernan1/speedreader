from goody       import safe_open
import goody
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friends_set = set()
    d = {}
    
    for line in file:
        friends_set.add(line)
    
    for i in friends_set:
           
        d[i.split(';')[0]] = i.split(';')[1:]
    
    return d


def print_graph(graph):
    matches = [(v, k) for (k, v) in read_graph.items(graph)]
    
    print(matches)
    
    


    

def find_influencers(graph):
    pass



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    
    print(graph) #delete later
   
    
    
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
