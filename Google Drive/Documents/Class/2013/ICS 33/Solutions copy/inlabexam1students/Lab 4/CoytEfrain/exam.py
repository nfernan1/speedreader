from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    list1 = [i.strip("\n") for i in file]
    dict1 = {}
    for i in list1:
        if i[0] not in dict1:
            dict1[i[0]] = {i[-1]}
            dict1[i[-1]] = set()
        else:
            dict1[i[0]].add(i[-1])
            dict1[i[-1]] = set()
    for person in dict1:
        for friend in dict1[person]:
            dict1[friend].add(person)
    return dict1

def print_graph(graph):
    print("\nGraph: source nodes (ordered) -> destination nodes (ordered)")
    for i in sorted(graph):
        print(i, "->", sorted(graph[i]))

def find_influencers(graph):
    infl = {i: len(graph[i])-ceil(len(graph[i])/2) for i in graph}
    cand = []
    for i in infl:
        if infl[i] >= 0:
            cand.append((infl[i],len(graph[i]),i))



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
