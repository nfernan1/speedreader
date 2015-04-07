# Irene Ng (95413809) Lab 3

from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
from goody       import read_file_values 


# Define your functions here.

def read_graph(file):
    graph = list(read_file_values(file))
    d = defaultdict(set)
    for line in graph:
        l = line.split(';')
        d[l[0]].add(l[1])
        d[l[1]].add(l[0])
    return dict(d)

        
    

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for k,v in sorted(graph.items()):
        print('  {} -> {}'.format(k, ', '.join(sorted(v))))
        

def find_influencers(graph):
    infl = {}
    for node in graph:
        infl[node] = len(graph[node])-ceil(0.5*len(graph[node]))
    while max(infl.values())>=0:
        cand = []
        for node in infl.keys():
            if infl[node]>=0:
                cand.append((infl[node],len(graph[node]),node))
        least = min(cand)[2]
        del infl[least]
        for friend in graph[least]:
            if friend in infl:
                infl[friend] = infl[friend]-1
    return set(infl.keys())
        
        
    
    
    
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('\nInfluencers =', find_influencers(graph))
