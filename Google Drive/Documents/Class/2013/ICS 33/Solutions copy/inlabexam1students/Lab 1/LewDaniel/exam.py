from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friend_dict = {}
    for line in file.readlines():
        line = line.strip('\n')
        split_line = line.split(';')
        if split_line[0] not in friend_dict:
            friend_dict[split_line[0]] = {split_line[1]}
        elif split_line[0] in friend_dict:
            friend_dict[split_line[0]].add(split_line[1])
        if split_line[1] not in friend_dict:
            friend_dict[split_line[1]] = {split_line[0]}
        elif split_line[1] in friend_dict:
            friend_dict[split_line[1]].add(split_line[0])
    return friend_dict

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    list_keys = [item for item in graph]
    for key in sorted(list_keys):
        value_list = [friend for friend in graph[key]]
        print(' ', key, ' -> ', ', '.join(sorted(value_list)))

def find_influencers(graph):
    infl = {k: len(graph[k]) - ceil(len(graph[k])/2) for k in graph}
    while True:
        cand = []
        for key in infl: 
            if infl[key] >= 0:
                cand.append(((infl[key]), (len(graph[key])), (key)))
        if cand == []:
            break
        lowest = min(cand)
        infl.pop(lowest[2])
        for node in graph:
            if lowest[2] in graph[node]:
                if node in infl:
                    infl[node] -= 1
    final = [item for item in infl.keys()]
    return set(final)
    


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
