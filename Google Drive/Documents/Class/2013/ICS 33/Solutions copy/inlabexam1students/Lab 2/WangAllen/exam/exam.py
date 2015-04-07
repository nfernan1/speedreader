from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    read_file = file.readlines()
    d = defaultdict(set)
    node_list = [(node[0],node[2]) for node in read_file]
    for item1, item2 in node_list:
        d[item1].add(item2)
    return d
        
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for node in sorted(graph):
        friend_list = [friend for friend in graph[node]]
        friend_list.sort()
        friends = ', '.join(friend_list)
        print('    {} -> {}'.format(node,friends))
        

def find_influencers(graph):
    infl = {node:(len(graph[node])-ceil(len(graph[node])/2)) for node in graph}
    cand = [(infl[key], graph[key], key) for key in infl if infl[key] < 0]
    while x > 0 for x in infl.values():
        min_val0 = min([val1[0] for val1 in cand])
        list_to_remove0 = [each for each in cand if each[0] == min_val0]
        if len(list_to_remove0) > 1:
            min_val1 = min([val1[1] for val1 in cand])
            list_to_remove1 = [each for each in cand if each[1] == min_val1]
            if len(list_to_remove1) > 1:
                cand.remove(x if x[2] == min(infl.values()))
                infl[x[2]]-1
                continue
            cand.remove(list_to_remove1[0])
            infl[(list_to_remove1[0])[2]]-1
            continue
        cand.remove(list_to_remove0[0])
        infl[(list_to_remove0[0])[2]]-1
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    #core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
