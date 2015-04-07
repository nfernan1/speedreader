from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    content = file.read().split('\n')
    newdict = {}
    for i in content:
        if i[0] in newdict:
            newdict[i[0]].add(i[2])
        else:
            newdict[i[0]] = set(i[2])
        if i[2] in newdict:
            newdict[i[2]].add(i[0])
        else:
            newdict[i[2]] = set(i[0])
    return newdict


def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for i in sorted(graph.keys()):
        print('{} -> {}'.format(i, sorted(graph[i])))
        

def find_influencers(graph):
    infl = dict()
    cand = []
    for i in sorted(graph.keys()):
        infl[i] = len(graph[i]) - ceil((len(graph[i])/2))
        cand.append((infl[i], len(graph[i]), i))
    while len(cand) > 0:
        c = min(cand)
        del infl[c[-1]]
        for i in sorted(infl.keys()):
            if c[-1] in graph[i]:
                infl[i] -= 1
                if infl[i] < 0:
                    for j in cand:
                        if i in j:
                            cand.remove(j)
        cand.remove(c)
    return set(infl)



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
