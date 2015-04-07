from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph_dict = {}
    
    with open(file, 'r') as f:
        data = f.read().splitlines()
        for info in data:
            datasplit = info.split(';')
            for key, val in zip(datasplit[0],datasplit[1]):
                if key in graph_dict:
                    graph_dict[key].add(val)
                else:
                    graph_dict[key] = set(val)

                if val in graph_dict:
                    graph_dict[val].add(key)
                else:
                    graph_dict[val] = set(key)
                    
    return graph_dict


def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for key, val in sorted(graph.items()):
        print('   {} -> {}'.format(key,val))
    print()
        
  

def find_influencers(graph):
    infl = {}
    cand = []
    for key, val in graph.items():
        print(val)
        infl[key] = (len(val) - ceil(len(val)/2))
        cand.append((infl[key], len(graph[key]), key))
        
    for i in range(len(cand)):
        for key in graph.keys():
            if cand[i][2] == key:
                pass
#         while (infl[key] >= 0):
#             for i in range(len(cand)):
#                 if cand[i][0] == 0:
#                     infl.pop(cand[i][2])
# 
#                     infl[key] -= 1 
    
    return infl.keys()

                    
                    


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
