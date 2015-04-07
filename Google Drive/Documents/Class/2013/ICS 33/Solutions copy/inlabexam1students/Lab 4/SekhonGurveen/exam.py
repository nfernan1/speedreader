from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file): 
    #takes open file and reads it, storing graph as dict
    #each node name = key
    #value = set of node names of friends
    graph_dict = defaultdict(set)
    content = file.readlines()
    for item in content:
        item = item.strip().split(';')
        graph_dict[item[0]].add(item[1])
        graph_dict[item[1]].add(item[0])
    return dict(graph_dict.items())

def print_graph(graph):
    #takes graph (a dict) and prints each node in alphabetical order
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for c,v in sorted(graph.items()):
        v = sorted(v)
        strv = v.pop(0)
        for item in v: strv += ', ' + item    
        print('{} -> {}'.format(c,strv))


def find_influencers(graph):
    #takes graph (a dict) and returns small set that contains influencer nodes
    infl = dict() #keys are every node name in graph, value = # of friends - 1/2(# of friends)
    cand = []
    for node, friends in graph.items():
        infl[node] = len(friends) - ceil(len(friends)/2)
        if infl[node] >= 0: cand.append((infl[node], len(friends), node))  
    
    while len(infl) > 1:
        cand = sorted(cand)
        min_v = cand.pop(0)
        for k in graph.keys():
            #print(k)
            if min_v[2] in infl: 
                del infl[min_v[2]]
            if min_v in graph[k]: 
                infl[k] = infl[k] - 1
        #for value in list(infl.values()):
            #if value <= 0: break 
         
            

    #print(infl)
    #print(cand)
    return set(infl.keys())




# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
