from goody       import safe_open, read_file_values
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    r = list(read_file_values(file))
    graph = dict()
    for each in r:
        each = each.split(';')
        if each[0] not in graph:
            graph[each[0]] = {each[-1]}
        elif each[0] in graph:
            graph[each[0]].add(each[-1])
        if each[-1] not in graph:
            graph[each[-1]] = {each[0]}
        else:
            graph[each[-1]].add(each[0])
    return graph

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for each in sorted(graph):
        x = ', '.join(each for each in sorted(graph[each]))
        print(each, '->', x)

def find_influencers(graph):
    infl, cand, minimum = dict(), [], []
    for node in graph:
        friends = len(graph[node])
        infl[node] = friends - ceil(friends/2)
        if infl[node] >= 0:
            cand.append((infl[node], friends, node))
    while (len(infl[each]) > 0 for each in infl):
        minimum = min(cand)
        infl.pop(minimum[-1])
        cand.remove(minimum)
        print('infl =', infl)
        print('cand =', cand)
        print('removing {} as key from infl; decrementing friends values'.format(minimum[-1]))
    return infl



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))

    print_graph(graph)
    find_influencers(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
