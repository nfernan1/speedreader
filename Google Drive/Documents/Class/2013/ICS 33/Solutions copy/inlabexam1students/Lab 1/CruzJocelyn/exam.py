from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    '''Couldn't get e,f,h,j in the dictionary'''
    
    graph = defaultdict(set)
    
    for line in file:
        k,v =  line.strip().split(';')
        graph[k].add(v)
    
    for key in graph:
        for v in graph[key]:
            if v in graph.keys():
                graph[v].add(key)
               
    return (graph)


def print_graph(graph):
    '''Prints the {} around the values'''
    
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    
    for k, v in sorted(graph.items()):
        print(' ', k, '->', v)


def find_influencers(graph):
    infl = dict()
    cand = []
    
    '''influence dictionary'''
    for k, v in graph.items():
        friends = len(v) - ceil(len(v)/2)
        infl[k] = friends 
    
    '''candidate list'''
    for l, m in graph.items():
        cand.append((infl[l], len(m), l))
        
    '''Getting the key that will be removed'''
    rem_key = ' '
    for key in infl.keys():
        prev = key
        if infl[key] < infl[prev]:
            rem_key = key
    
    '''Subtracting the key'''
    del(infl[rem_key])
    
               
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
    
