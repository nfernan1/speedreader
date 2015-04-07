from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    lines = file.read().split()
    friend_dict = defaultdict(set)
    for line in lines:
        names = line.split(sep=';')
        friend_dict[names[0]].add(names[-1])
        friend_dict[names[-1]].add(names[0])
    
    return dict(friend_dict)

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for key in sorted(graph.keys()):
        print('{} -> {}'.format(key,', '.join(sorted(graph[key]))))

def find_influencers(graph):
    infl = defaultdict(int)
    for key in graph.keys():
        friends = len(graph[key])
        half = ceil(friends/2)
        infl[key]=friends - half
    while True:
        cand = []
        for key in infl.keys():
            if infl[key]>=0:
                cand.append( (infl[key],len(graph[key]),key) )
        if cand == []:
            break
        cand = sorted(cand)
        min_key = cand[0][-1]
        infl.pop(min_key)
        for key in infl.keys():
            if min_key in graph[key]:
                infl[key]-=1
    
    return set(infl.keys())
        
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r','Could not find that file'))
    print_graph(graph)
    print()
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
