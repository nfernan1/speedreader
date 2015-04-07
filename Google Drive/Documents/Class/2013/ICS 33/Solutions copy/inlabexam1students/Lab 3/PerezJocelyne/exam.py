from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in open(file):
        a,b = line.strip().split(';')
        graph[a].add(b)
    return graph


def print_graph(graph):
    print('Graph: source nodes (ordered -> destination nodes (ordered)')
    for a in sorted(graph.keys()):
        print('  {} -> {}'.format(a,sorted(graph[a])))

def find_influencers(graph):
    infl = defaultdict(set)
    cand =[]
    for node in graph.keys():
        friends = len(graph.get(node))
        num = ceil(friends)-(friends/2)
        infl[node] = friends-ceil(len(graph.get(node))/2)
        cand.append((infl[node],friends,node))
    while cand != []:
        rem = min(cand)
        cand.remove(rem)
        del infl[rem[2]]
        for a in infl:
            if rem in infl[a]:
                infl[a].pop(rem)
    return infl.keys()

    
    
graph = read_graph('graph.txt')
print_graph(graph)
find_influencers(graph)

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
