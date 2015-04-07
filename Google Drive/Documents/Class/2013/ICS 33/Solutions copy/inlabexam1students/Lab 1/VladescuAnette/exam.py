from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = {}
    additional = {}
    
    ## need to get values to become keys as well --> explore and reached lists in reachable problem
    for line in file:
        line = line.strip('\n').split(';')
         
        if line[0] not in graph:
            graph[line[0]] = {line[1]}
          
        else:
            graph[line[0]].add(line[1])
               
    return graph       


def print_graph(graph): 
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    keys = []
    for key in graph.keys():
        keys.append(key)
         
    keys.sort()
    for key in keys:
        print('  {} -> {}'.format(key, graph[key]))
    
        

def find_influencers(graph):
    inf = {}
    cand = []
    
    for i in graph:
        inf[i] = ceil(len(graph[i]) - (len(graph[i])/2))
     
    
    ##  while loop that checks that the values are not negative
    for key in inf:
        cand.append((inf[key], len(graph[key]), key))
            
    ## find the min in the cand list of tuples
    
    ## remove min value's key
    
            
    

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    

    print_graph(graph)
    core = find_influencers(graph)
    

    
    print('Influencers =', find_influencers(graph))
