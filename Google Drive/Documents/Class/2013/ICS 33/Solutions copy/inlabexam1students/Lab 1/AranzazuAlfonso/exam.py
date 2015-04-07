from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    outter_dict = dict()
    
    inner_dict = dict()
    
    for line in file.readlines():
        split_lines = line.strip().split(';')
        if split_lines[0] not in inner_dict:
            inner_dict[split_lines[0]] = split_lines[1]
        else:
            inner_dict[split_lines[0]].add(split_lines[1])
    outter_dict.update(inner_dict)
    return outter_dict
    


def print_graph(graph):
    print("Graph: source nodes (ordered) -> destination nodes (ordered)")
    
    for c, v in sorted(graph.items()):
        print(c, '->', v)

def find_influencers(graph):
    infl = dict()
    for k,v in graph.items():
        infl[k] = (len(v) - ceil(len(v)/2))
    
    candidates = []
    while candidates != []:
        for c, v in infl.items():
            candidates.append( (v, '', c) )
    
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
   
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
    