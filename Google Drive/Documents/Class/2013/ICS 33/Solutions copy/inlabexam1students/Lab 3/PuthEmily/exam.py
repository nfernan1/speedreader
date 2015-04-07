from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    read_graph = file.readlines()
    graph = {}
    for line in read_graph:
        l = line.strip().split(';')
        if l[0] in graph.keys():
            graph[l[0]].add(l[1])
        else:
            graph[l[0]] = set(l[1])
    for line in read_graph:
        l = line.strip().split(';')
        if l[1] in graph.keys():
            graph[l[1]].add(l[0])
        else:
            graph[l[1]] = set(l[0])
    return graph
      
  
def print_graph(graph):
    sorted_graph = sorted(graph.items())
    for key, value in sorted_graph:
        print('{} -> {}'.format(key, value))
 
 
def find_influencers(graph):
    influence = {}; candidates = [1]
    while True:
        
        if len(candidates) != 0:
            for key, value in graph.items():
                influence[key] = len(value) - ceil(len(value)/2)
            print(influence)
            cand = [];
            for i in influence:
                if influence[i] >= 0:
                    cand.append((influence[i], len(graph[i]), i)); candidates = cand
            for i in candidates:
                if i[0] == 0:
                    graph.pop(i[2])
                    for key, values in graph.items():
                        if i[2] in values:
                            graph[key].remove(i[2])
        else:
            return influence



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print(core)
#     print('Influencers =', find_influencers(graph))
