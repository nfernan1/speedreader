from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
import collections

# Define your functions here.

def read_graph(file):    
    result = defaultdict(set)
    for line in file.readlines():
        temp = line.split(';')
        if temp[-1][-1] == '\n':
            result[temp[0]].add(temp[-1][:-1])
            result[temp[-1][:-1]].add(temp[0])
        else:
            result[temp[0]].add(temp[-1])
            result[temp[-1]].add(temp[0])
    return dict(result)
        

def print_graph(graph):
    print('Graph: source nodes (orderded) -> destination nodes (ordered)')
    for item in sorted(graph.items()):
        print('  {} -> {}'.format(item[0],', '.join(sorted(item[1]))))

def find_influencers(graph):
    infl,cand,result = {},[],set()
    for item in graph.items():
        infl[item[0]] = len(item[1])-ceil(len(item[1])/2)
    for item in infl.items():
        cand.append((infl[item[0]],len(graph[item[0]]),item[0]))
    while cand != []:
        node = sorted(cand).pop(0)[-1]
        del infl[node]
        for item in infl:
            if node in graph[item]:
                infl[item] = infl[item] -1
        cand = []
        for item in infl.items():
            if infl[item[0]] >= 0:
                cand.append((infl[item[0]],len(graph[item[0]]),item[0]))
    for item in infl:
        result.add(item)
    return result
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
