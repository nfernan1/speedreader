from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    dic = dict()
    for i in file:
        x = i.split(';')
        a = x[0]
        b = x[1].rstrip('\n')
        if a in dic.keys():
            dic[a].add(b)
        else:
            dic[a] = {b}
        if b in dic.keys():
            dic[b].add(a)
        else:
            dic[b] = {a}
    return dic
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for k, v in sorted(graph.items()):
        print(str(k) + ' -> ' + str(', '.join(sorted((i for i in v)))))      

def find_influencers(graph):
    infl = dict()
    for k, v in graph.items():
        infl[k] = len(v)-ceil(len(v)/2)
    cand = []
    for k, v in infl.items():
        cand.append((v, len(graph[k]), k))
    while cand != []:
        x = min(cand)
        for k in infl.keys():
            if k in graph[x[2]]:
                infl[k] -= 1
        del infl[x[2]]
        cand = []
        for k, v in infl.items():
            if v < 0:
                pass
            else:
                cand.append((v, len(graph[k]), k))
    newset = set()
    for i in infl.keys():
        newset.add(i)
    return newset
    
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
