from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
import goody


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in file.readlines():    
        k, v = line.split(';')
        graph[k.strip()].add(v.strip())
        if k not in graph[v]:
            graph[v].add(k.strip())
    return graph

def print_graph(graph):
    for k, v in sorted(graph.items()):
        print(k, ' -> ',  v)


def find_influencers(graph):
    # node names and important information
    infl = {}
    cand = []
    
    for k, v in graph.items():
        infl[k] = len(v) - ceil(len(v)/2)
        
    for k, v in infl.items():
        if not v < 0:
            cand.append((v, len(graph[k]), k))
    
    cand.sort(reverse = True)
    removed = cand.pop()
    print("Removing ", removed[2], " as key from infl; decrementing friend's values")
    
    infl[removed[2]] -= 1









# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
