from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    d=defaultdict(set)
    for lines in file:
        s,a=lines.strip().split(';')
        d[s].add(a)
    return d
    
def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for a,b in sorted(graph.items()):
        print(a,'->', sorted(b))

def find_influencers(graph):
    infl={};candidates=[]
    for key,value in graph.items():
        infl[key]=(len(value)-ceil(len(value)/2))
        if  infl[key] >= 0:
            candidates.append((infl[key], len(value), key))
    for x in candidates:
        if x[0] <= 0:
            del infl[x[2]]
            for key,value in graph.items():
                if x[2] in graph[key]:
                    infl[key]=infl[key]-1
    return set(infl.keys())




# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
