from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friends = {}
    files = open(file)
    f = files.read().split()
    for item in f:
        if item[0] in friends.keys():
            friends[item[0]].update(item[-1])
        else:
            friends[item[0]] = {item[-1]}        
    return friends
        

def print_graph(graph):
    print('Graph:  source nodes (ordered) -> destination nodes (ordered)')
    for k, v in sorted(graph.items()):
        print("  {} -> {}".format(k, v))

def find_influencers(graph):
    infl = {}
    for k, v in sorted(graph.items()):
        infl[k] = (len(v) - ceil(len(v)/2))
    cand = []
    while infl.values() >= 0:
        for k, v in infl.items():
            if len(k) >= 0:
                cand.append((v,len(k),k))
        min = 0
        for item in cand:
            if item[0] <= min:
                cand.remove(item)
        
    return cand
        



# Script

if __name__ == '__main__':
    print(read_graph('graph.txt'))
    x = read_graph('graph.txt')
    print(find_influencers(x))
  
#     graph = read_graph(safe_open('Enter name of file with graph', 'r',
#                                  'Could not find that file'))
#     print_graph(graph)
#     core = find_influencers(graph)
#     print('Influencers =', find_influencers(graph))
