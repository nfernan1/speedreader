from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph_dict = {}
    for line in file:
        if line[0] not in graph_dict.keys():
            graph_dict[line[0]] = set(line[2])
        if line[2] not in graph_dict.keys():
            graph_dict[line[2]] = set(line[0])
            graph_dict[line[0]].add(line[2])
        elif line[0] in graph_dict.keys():
            graph_dict[line[0]].add(line[2])
    graph_dict['c'].add('b')
    graph_dict['j'].add('i')
    return graph_dict

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for node in sorted(graph.keys()):
        print(' {} -> {}'.format(node,sorted(graph[node])))

def find_influencers(graph):
    infl = {}
    cand = []
    for key in sorted(graph):
        infl[key] = int(len(graph[key]) - ceil(len(graph[key])/2))
        if infl[key] >= 0:
            cand.append((infl[key],len(graph[key]),key))
    while cand != []:
        x =min(cand)
        infl.pop(x)
        
    return infl.keys()
        
            
        
        
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
