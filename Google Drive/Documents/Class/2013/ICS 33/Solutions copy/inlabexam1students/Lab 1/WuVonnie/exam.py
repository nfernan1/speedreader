from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph_dict = {}
    
    for line in file:
        Line = line.strip().split(';')
        if Line[0] not in graph_dict.keys():
            graph_dict[Line[0]] = set(Line[-1])
        else:
             graph_dict[Line[0]].add(Line[-1])
             
        if Line[-1] not in graph_dict.keys():
            graph_dict[Line[-1]] = set(Line[0])
        else:
            graph_dict[Line[-1]].add(Line[0])
     
    return graph_dict
        

def print_graph(graph):
    print ('\n Graph: soure nodes (ordered) -> destination nodes (ordered)')
    for c,v in sorted(graph.items()):
        destination_node = ', '.join(value for value in v)
        print ("   {} -> {}".format(c, destination_node))


def find_influencers(graph):
    infl = {}
    cand = []
    
    for k in graph.keys():
        infl[k] = (len(graph[k])- ceil(len(graph[k])/2))
            
    cand = [tuple([infl[k], len(graph[k]), k]) for k in infl.keys() if infl[k] >= 0]
     
    first_min = min(''.join(str(tup[0]) for tup in cand))
    second_min = min(''.join(str(tup[1]) for tup in cand))
    third_min = min(''.join(str(tup[2]) for tup in cand))
    
    for i in range(len(cand)-1):
        if cand[i][i] == first_min:
            pass
    
        
    
    
    



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
    
