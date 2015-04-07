from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friend_graph = {}
    for line in file:
        friend = line.strip().split(';')
            
        if friend[0] not in friend_graph:
            friend_graph[friend[0]] = set(friend[1])
        if friend[1] not in friend_graph:
            friend_graph[friend[1]] = set(friend[0])
        if friend[0] in friend_graph:
            friend_graph[friend[0]].add(friend[1])
        if friend[1] in friend_graph:
            friend_graph[friend[1]].add(friend[0])

    return friend_graph



def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    
    for key in sorted(graph):
        print('{} -> {}'.format(key, sorted(graph[key])))

def find_influencers(graph):
    infl = {}
    cand = []
    
    for key in graph:
        infl[key] = len(graph[key]) - ceil(len(graph[key])/2)

    while True:
        for key in infl:
            cand.append((infl[key], len(graph[key]), key))
#         if min(cand)[0] == -1: #
#             break #
        
        count = 0 #
        for i in cand:
            if i[0] == -1:
                count += 1
        if count == len(cand):
            break #
        
        minimum = min(cand)[2]    
        del(infl[minimum])
        for friend in graph[minimum]:
            infl[friend] -= 1
        cand = []
        
    return infl.keys()
    





# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
