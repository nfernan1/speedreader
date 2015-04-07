from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = file.readlines()
    graph_dict = defaultdict(set)
    for x in graph:
        x = x.strip().split(';')
        graph_dict[x[0]].add(x[1])
    print(graph_dict)
    return graph_dict
    
def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination (ordered)')
    for key in graph:
        print('{}->{}').format(key, graph[key])

    
def find_influencers(graph):
    #subtractive algorithm
    infl = {}
    cand = []
    for key in graph:
        infl.update({key: (len(graph[key])-ceil(len(graph[key])/2))})
    
    while len(infl) > 0:
        for k in infl:
            cand.append((infl[k], k))



    #I didn't finish

    
    
    
        
        
        
        
    



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
