from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    new_dict = dict()
    for line in file.readlines():
        line = line.strip().split(';')
        if line[0] not in new_dict:
            new_dict[line[0]] = set(line[1])
            new_dict[line[1]] = set(line[0])
        if line[0] in new_dict:
            new_dict[line[0]].add(line[1])
    copy_dict = new_dict.copy()
    for key in copy_dict:
        for value in copy_dict[key]:
            if value not in new_dict:
                new_dict[value] = set(key)
            else:
                new_dict[value].add(key)
    return new_dict

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for key in sorted(graph):
        print(' ',key, '->', str(sorted(graph[key])))

def find_influencers(graph):
    infl = dict()
    for key in graph:
        infl[key] = len(graph[key]) - ceil(len(graph[key])/2)
    while len(infl) != 0:
        cand = []
        for item in infl:
            if infl[item] >= 0:
                cand.append((infl[item], len(graph[item]), item))
        minimum = min(cand) if len(cand) != 0 else None
        if minimum != None:
            del infl[minimum[2]]
            for i in infl:
                if minimum[2] in graph[i]:
                    infl[i] = infl[i] - 1
        else:
            return set(infl.keys())



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print()
    print_graph(graph)
    core = find_influencers(graph)
    print()
    print('Influencers =', find_influencers(graph))
