from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
import re


# Define your functions here.

def read_graph(file):
    friendships = file.read().split('\n')
    
    result = defaultdict(set)
    for formatthis in friendships:
        ship = formatthis.split(';')
        result[ship[0]].update(set(ship[1]))
        result[ship[1]].update(set(ship[0]))
     
    return dict(result)

def print_graph(graph):
    print('\nGraph:source nodes (ordered) -> destination nodes (ordered)')
    for key in sorted(graph):
        friends = (friend for friend in sorted(graph[key]))
        print('  {} -> {}'.format(key, ', '.join(friends)) )
        
        
def find_influencers(graph):
    infl = dict()
    
    for key in graph:
        num_f = len(graph[key])
        infl[key] = num_f - ceil(num_f/2)
        

    while max(infl.values()) >= 0 :
        cand = [(infl[key],len(graph[key]), key) for key in infl if infl[key] >= 0]
        remove = min(cand)
        
        for key in infl:
            if remove[2] in graph[key]:
                infl[key] -= 1
                
        infl.pop(min(cand)[2])

    return set(infl.keys())


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    
    print_graph(graph)
    core = find_influencers(graph)
    print('\nInfluencers =', find_influencers(graph))
