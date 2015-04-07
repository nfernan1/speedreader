from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    my_dict = defaultdict(set)
    
    for i in file.readlines():
        my_dict[i[0]].add(i[2])
        my_dict[i[2]].add(i[0])
        

    return my_dict
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    my_format = '{} -> {}'
    for k in sorted(graph):
        print (my_format.format(k, str(sorted(graph[k]))))
        
        
        
        
        

def find_influencers(graph):
    infl = {}
    
    for k in graph:
        infl[k] = len(graph[k]) - ceil(len(graph[k])/2)
        
    while len(infl)>= 0:
        cand = [ (infl[k], len(graph[k]), k) for k in infl if infl[k] >= 0]
        min_val = min(cand)
        infl.remove(min_val[2])
        infl[min_val[2]] -= 1
        
    
    return infl



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
