from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friends = defaultdict(set) 
    for line in file.readlines():
        k,v = line.rstrip().split(';')[0], line.rstrip().split(';')[1]
        friends[k].add(v)
        friends[v].add(k)
        
    return(friends)

def print_graph(graph):
    for node, dest in sorted(graph.items()):
        destinations = ''
        #destinations.join(for desti in dest)
        for desti in sorted(dest):
            destinations = destinations + desti + ', '              
        print(node, '->' , destinations)


def find_influencers(graph):
    infl = {}
    for node, dest in sorted(graph.items()):
        infl[node] = (len(dest)- ceil(len(dest)/2))
   
    while True:
        print('infl = ',infl)
        cand = []
        for candidate, nfriends in infl.items():
            #if nfriends >= 0:
            cand.append((nfriends, len(graph[candidate]), candidate))  
        print('cand = ', cand)
        
        minimun = min(cand)
        print('removing ', minimun[2], 'as key')
        infl.pop(minimun[2])
        #=====c=========
        for node, value in graph.items():
            if minimun[2] in value:
                infl[node] -= 1
        
    
    
# Script
if __name__ == '__main__':

    graph = read_graph(safe_open('Enter name of file with graph', 'r','Could not find that file'))
    
    print_graph(graph)
    #core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
