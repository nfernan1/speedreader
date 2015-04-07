from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict

# Define your functions here.

def read_graph(file) -> dict:
    graph = defaultdict(set)
    lines = file.readlines()
    good_lines = []
    for line in lines: good_lines.append(line.strip().split(';'))
    for pair in good_lines:
        graph[pair[0]].add(pair[1])
        graph[pair[1]].add(pair[0])
    return dict(graph)

def print_graph(graph):
    print("\nGraph: source nodes (ordered) -> destination nodes (ordered)")
    for person in sorted(graph):
        friend_str = ''
        for friend in sorted(graph[person]): friend_str = friend_str+friend+', '
        print('  {} -> {}'.format(person, friend_str.strip().strip(',')))

def find_influencers(graph) -> set:
    infl = dict()
    for person in graph: infl[person] = len(graph[person])-ceil(len(graph[person])/2)
    cand=[(infl[c], len(graph[c]), c) for c in infl]
    while len(cand)>0:
        min_c = min(cand)
        cand.remove(min_c)
        del infl[min_c[2]]
        for person2 in graph:
            if (min_c[2] in graph[person2]) and (person2 in infl):
                infl[person2] -= 1
        cand=[(infl[c], len(graph[c]), c) for c in infl if infl[c] >= 0]
    return set(infl.keys())

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('\nInfluencers =', find_influencers(graph))
