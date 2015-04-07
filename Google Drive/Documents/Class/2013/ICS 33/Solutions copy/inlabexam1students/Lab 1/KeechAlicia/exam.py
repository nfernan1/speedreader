from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    read_lines = [i.strip().split(';') for i in file.readlines()]
    graph_dict = defaultdict(set)
    for k,v in read_lines:
        graph_dict[k].add(v)
        graph_dict[v].add(k)
    return dict(graph_dict)

def print_graph(graph):
    print('\nGraph: source nodes(ordered) -> destination nodes (ordered)')
    for k,v in sorted(graph.items()):
        print('{} -> {}'.format(k,', '.join(sorted(v))))
    print()

def find_influencers(graph):
    infl = defaultdict(set)
    for k,v in graph.items():
        infl[k] = len(v) - ceil(len(v)/2)
    while True:
        cand = [(j, len(graph[i]), i) for i,j in infl.items() if j >= 0]
        if len(cand) == 0:
            return set(infl.keys())
        minval = sorted(cand)[0][2]
        del(infl[minval])
        for g in infl.keys():
                infl[g] -= (1 if minval in graph[g] else 0)



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
