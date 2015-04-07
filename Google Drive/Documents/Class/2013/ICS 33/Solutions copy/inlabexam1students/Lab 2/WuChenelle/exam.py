from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friends = {}
    for line in open(file):
        p = line.strip('\n').split(';')
        if p[0] not in friends:  
            friends[p[0]] = set(p[1])
        else:
            friends[p[0]].add(p[1])
        if p[1] not in friends:
            friends[p[1]] = set(p[0])
        else:
            friends[p[1]].add(p[0])
    return friends     

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for c in sorted(graph):
        y = {t for t in sorted(graph[c])}
        k = ', '
        print('{0} -> {1}'.format(c,k.join(y)))  

def find_influencers(graph):
    infl = {}
    cand = []
    for g in graph:
        b = len(sorted(graph[g])) - ceil(len(sorted(graph[g]))/2)
        infl[g] = b
        cand.append((b,len(sorted(graph[g])),g))
    while cand != []:
        for g in graph:
            if min(cand)[2] in graph[g]:
                d = str(int(infl[g])-1)
                infl[g] = d
                if g == cand[2]:
                    cand[0] = d
        infl.pop(min(cand)[2])
        cand.remove(min(cand))
        print(infl,cand)    
    else:
        s = set()
        for c, v in infl:
            s.add(c)
        return s
find_influencers(read_graph('graph.txt'))   


# Script

# if __name__ == '__main__':
#     graph = read_graph(safe_open('Enter name of file with graph', 'r',
#                                  'Could not find that file'))
#     print_graph(graph)
#     core = find_influencers(graph)
#     print('Influencers =', find_influencers(graph))
