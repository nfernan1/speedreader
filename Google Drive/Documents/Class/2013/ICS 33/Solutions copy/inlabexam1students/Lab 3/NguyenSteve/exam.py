from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    newfile = file.readlines()
    d = {}
    aset = set()
    for key in newfile:
        if key[0] not in d:
            d.update({key[0]:set(key[2])})
        else:
            d[key[0]].add(key[2])
    return d         
            
            

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for item in graph.keys():
        print('{} -> {}'.format(item, graph.get(item)))
    
    
def find_influencers(graph):
    infl = {}
    aset = set()
    cand = []
    
    for node in graph:
        half = ceil(len(graph.get(node))/2)
        infl.update({node:half})
        cand.append((half, len(graph.get(node)), node))
    print('infl =', infl)
    print('cand =', cand)
    while True:
        for value in infl.values():
            if value < 0:
                return aset
            else:
                for can in cand:
                    if can[1] == 0:
                        infl.pop(index[can[1]])
                        print('removing as key from infl: decrementing friend"s values')
            
                



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
