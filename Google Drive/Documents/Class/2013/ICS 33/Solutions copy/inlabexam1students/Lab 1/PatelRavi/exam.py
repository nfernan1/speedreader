from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    node = {}
    for line in file:
        line_edit = line.strip().split(';')
        source = line_edit[0]
        if source not in node:
            node[source] = set(line_edit[1])
        else:
            node[source].update(line_edit[1])
    return(node)
            
            

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for line in sorted(graph):
        print(' ', line, '->', graph[line])
    

def find_influencers(graph):
    infl = dict()
    cand = list()
    for line in graph.keys():
        infl[line] = ceil(len(graph[line])/2)
    for i in infl.keys():
        if infl[i] > 0:
            cand.append([infl[i], len(graph[i]), i])

        
    
        
    
    


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
