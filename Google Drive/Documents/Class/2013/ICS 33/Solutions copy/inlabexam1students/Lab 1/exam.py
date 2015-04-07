from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    GraphDict = {}
    for line in file.readlines():
        items = line.strip('\n').split(';')
        if items[0] in GraphDict:
            GraphDict[items[0]].add(items[1])
        else:
            GraphDict[items[0]] = {items[1]}
        if items[1] in GraphDict:
            GraphDict[items[1]].add(items[0])
        else:
            GraphDict[items[1]] = {items[0]}
    return GraphDict
    

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    sorted = []
    for key in graph:
        sorted.append(key)
    sorted.sort()
    for key in sorted:
#         vallist = list(graph[key])
#         vallist.sort()
        valstr = ','.join(graph[key])
#         valstr = valstr.strip('[').strip(']')
        print(' ', key, ' -> ', valstr )
        
def find_influencers(graph):
    infl = {}
    for key in graph:
        myint = len(graph[key])
        infl[key] = (myint) - ceil(myint/2)
    cand = []
    for key in infl:
        if infl[key] >= 0:
            cand.append((infl[key], len(graph[key]), key))
    cand.sort()
    while len(cand) > 2:
        cand.remove(cand[0]) 
    return cand




# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print('GraphDict\n', graph)
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
