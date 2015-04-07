import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        s,d = line.rstrip().split(';')
        graph[s].add(d)
        graph[d].add(s)
    return graph


def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for s,d in sorted(graph.items()):
        print(' ',s,'->',", ".join(sorted(d)))


def find_influencers(graph):
    infl = {v:len(graph[v])-ceil(len(graph[v])/2) for v in graph}
    while True:
        cand = [(infl[v],len(graph[v]),v) for v in infl if infl[v]>=0]
        if not cand:
            return set(infl)
        i,f,v = min(cand)
        del infl[v]
        for v in graph[v]:
            if v in infl:
                infl[v] -= 1


    
if __name__ == '__main__':
    graph = read_graph(goody.safe_open('Enter name of file with graph', 'r', 'Could not find that file'))
    print_graph(graph)
    print('Influencers =', find_influencers(graph))
