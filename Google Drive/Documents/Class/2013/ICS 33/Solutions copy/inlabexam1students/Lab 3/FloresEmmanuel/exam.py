from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friends_dict = defaultdict(set)
    
    for line in file:
        friend = line.strip().split(';')
        node = friend[0]
        node_friend = friend[1] 
        
        
        friends_dict[node].add(node_friend)
        friends_dict[node_friend].add(node)
        
   
    return friends_dict
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for node in sorted(graph):
        friends = str(', ').join(graph[node])
        print('    {} -> {}'.format(node, friends))

def find_influencers(graph):
    infl = dict()
    for node in graph:
        num_friends = len(graph[node])
        half_friends = ceil(len(graph[node])/2)
        infl_val = num_friends - half_friends
        infl[node] = infl_val
    #bool = [True for i in infl.values() if i>-1]  
              
    while sum(infl.values())>-1:
        cand = []
        for i in infl:
            if infl[i]>-1:
                tup = (infl[i], len(graph[i]), i)
                cand.append(tup)
        
        
        min_can = min(cand)
        min_node = min_can[2]
        
        infl.pop(min_node)
        min_friends = graph[min_node]
        
        for node in min_friends:
            if node in infl:
                new_value = infl[node]-1
                infl[node] = new_value
    
    return set(infl.keys())
    
    
        
        
        
   
 



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
