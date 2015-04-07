from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friend_dict = defaultdict(set)
    lines = file.readlines()
    for line in lines:
        split_line = line.strip().split(";")
        friend_dict[split_line[0]].add(split_line[1])
        friend_dict[split_line[1]].add(split_line[0])
    
    return dict(friend_dict)
        

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for key in sorted(graph):
        print(' ' , key , '->' , ', '.join(sorted(graph[key])))

def find_influencers(graph):
    infl = {}
    for key in graph:
        infl[key] = len(graph[key]) - ceil(len(graph[key]) / 2)
   
    while True:
        all_neg = True
        cand = []
        for key in infl:
            if(infl[key] >= 0):
                all_neg = False
                cand.append((infl[key] , len(graph[key]) , key))
        if(all_neg):
            break
        cand.sort()
        del infl[cand[0][2]]
        for value in graph[cand[0][2]]:
            if(value in infl):
                infl[value] -= 1
        
    return set(infl.keys())
        
        
        
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('\nInfluencers =', find_influencers(graph))
