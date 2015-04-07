from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.
def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        s, d = line.strip().split(';')
        graph[s].add(d)
        graph[d].add(s)
    return graph
    
def print_graph(graph):
    print("Graph: source nodes (ordered) -> destination nodes (ordered)")
    for s in sorted(graph.keys()):
        print(' ',s, ' -> ', ', '.join(sorted(graph[s])))
        
def find_influencers(graph):
    infl = dict(graph)
    for k, v in infl.items():
        infl[k] = len(v) - ceil(len(v)/2)
    cand = []
    #while True:
    #couldn't get this part to continuously loop as it should, sorry
    for s, d in infl.items():
        cand_tup = (d, len(graph[s]), s)
        cand.append(cand_tup)
    sorted_cand = sorted(cand)
    min_cand = sorted_cand[0]
    del infl[min_cand[2]]


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
