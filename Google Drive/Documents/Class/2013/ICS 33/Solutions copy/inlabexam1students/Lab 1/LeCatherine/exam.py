from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict

#Catherine Le 54953778
# Define your functions here.

def read_graph(file):
    some_dict = {}
    for line in file:
        node = line.strip('\n').split(';')
        if node[0] in some_dict:
            some_dict[node[0]].add(node[1])
        else:
            some_dict[node[0]] = set(node[1])
            
        if node[1] in some_dict:
            some_dict[node[1]].add(node[0])
        else:
            some_dict[node[1]] = set(node[0])
            
    return some_dict

def print_graph(graph):
    for node in sorted(graph):
        print('{} -> {}'.format(node,', '.join(i for i in sorted(graph[node]))))

def find_influencers(graph):
    infl = {}
    cand = []
    for k in graph:
        if len(graph[k]) == 1:
            infl[k] = 0
        else:
            infl[k] = len(graph[k])-ceil(len(graph[k])/2)
    print(infl)
    for k in infl:
        if infl[k] >= 0:
            cand.append((infl[k],len(graph[k]),k))
        elif len(cand) == 0:
            break
        minimum = min(cand)
        return infl.pop(minimum[2])
    
            


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print(core)
    print('Influencers =', find_influencers(graph))
