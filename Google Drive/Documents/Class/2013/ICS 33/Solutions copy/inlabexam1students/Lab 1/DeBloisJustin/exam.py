from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file) -> dict:
    my_dict = defaultdict(set)
    
    
    for line in file.readlines():
        each_line = line.rstrip()
        my_line = each_line.split(';')
        
        my_dict[my_line[0]].add(my_line[1])
        
    return dict(my_dict)
        
def print_graph(graph: dict) -> None:
    keys = sorted(graph.keys())
    values = sorted(graph.values())
    
    print("Graph: source nodes (ordered) -> destination nodes (ordered)")
    for i in range(len(keys)):
        print("{} -> {}".format(keys[i], values[i]))
    
        

def find_influencers(graph: dict):
    infl = dict()
    for key in graph.keys():
        infl[key] = len(graph[key]) - ceil(len(graph[key])/2) #{'i': 0, 'd': 1, 'g': 1, 'a': 1, 'b': 0, 'c': 1}
    
    graph_keys = list(graph.keys())
    while True:
        cand = list()
         
        for key in graph_keys:
            if infl[key] >= 0:
                cand.append((infl[key], len(graph[key]), key))
                 
        current_low = ()
        for i in range(len(cand) -1): ##cand[i][-1] == node name
            if cand[i][0] < cand[i+1][0]:
                current_low = (cand[i], i)
                        
        graph_keys.remove(current_low[0][-1])
        
        del infl[current_low[0][-1]]
        
        cand.pop(current_low[-1])
        
        print("infl =", infl)
        print("cand =", cand)
        
        print("removing {} as key from infl; decrementing friends values".format(current_low[0][-1]))
        print()   
        
        for key in graph_keys:
            infl[key] = len(graph[key]) - ceil(len(graph[key])/2)  
                
      
        if len(cand) == 0:
            break
    return 
    
                
        
         
        




# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
