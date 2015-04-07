from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.
# usually k will stand for the word key, or default iterator in a loop; and v for value
def read_graph(file):
    lines = file.read().split('\n') 
    dd = dict()
    for line in lines:
        k,v = line.split(sep = ';')
        if k in dd:                   # if it already exists in dd, add additional value
            dd[k].add(v)
        elif k not in dd:
            dd[k] = set(v)      # if it does not exist, create it with given value
        if v in dd:                  # since each node is friends both ways, repeat
            dd[v].add(k)        # process to make each value a key also
        elif v not in dd:
            dd[v] = set(k)
    return dd
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for key in sorted(graph.keys()):
        print('{} -> {}'.format(key,set(sorted(graph[key]))))

def find_influencers(graph):
    infl = dict()
    cand = []   # create list of candidates
    for k in sorted(graph.keys()):              # Part 1 of the problem
        infl[k] = (ceil(len(graph[k]) / 2))     
        cand.append(infl[k], len(graph[k]), k)
    while len(cand) > 0:
        m = min(cand)
        for b in sorted(graph.keys()):              # exclude those with negative keys
            if m[-1] in graph[b]:
                graph[b].remove[m[-1]]
                infl[b] -= 1
                if infl[b] < 0:
                    for var in cand:
                        if b is var:
                            cand.remove(var)
                        
                                        
        
        
        


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
