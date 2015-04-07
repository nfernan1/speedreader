from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    my_dict = defaultdict(set)
    k = file.readlines()
    for item in k:
        _strip = item.strip()
        _split = _strip.split(';')
        my_dict[_split[0]].add(_split[1])
        my_dict[_split[1]].add(_split[0])
        
    return my_dict
    

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes(ordered)')
    for key in sorted(graph.keys()):
        print('{} -> {}'.format(key, ', '.join(sorted(graph[key]))))
              

def find_influencers(graph):
    infl = {}
    cand = [] 
    for item in graph.keys():
        infl[item] = len(graph[item]) - (ceil(len(graph[item]) / 2))
        
    for key in infl.keys():
        if infl[key] < 0:
            continue
        else:
            cand.append(tuple([infl[key],len(graph[key]),key]))
    while True:
        min_list = tuple(cand) 
        min_ = cand[0][0]      
        for item in min_list:
            if item[0] < min_:
                min_ = item[0]
        for item in min_list:
            if item[0] != min_:
                min_list = min_list.remove(item)
    return(min_list)
    
            
        
        
        
        
        

    return infl , cand
            


# Script
if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
