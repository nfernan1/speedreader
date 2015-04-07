from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    final = {}
    for line in file.readlines():
        line = line.strip().split(';')
        if line[0] not in final.keys():
            final[line[0]] = set()
        if line[1] not in final.keys():
            final[line[1]] = set()
        final[line[0]].add(line[1])
        final[line[1]].add(line[0])
    return final

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for i in sorted(graph.keys()):
        print('  {} -> {}'.format(i,', '.join(sorted(graph[i]))))

def find_influencers(graph):
    infl = {}
    for i in graph.keys():
        infl[i] = len(graph[i])-ceil(len(graph[i])/2)
    while True:
        cand = []
        for i in infl.keys():
            if infl[i] >= 0:
                cand.append((infl[i],len(graph[i]),i))
        print('infl = ',infl)
        print('cand = ',cand)
        print("removing",min(cand)[2],"as key from infl; decrementing friends's values\n")
        for i in graph[min(cand)[2]]:
            if i in infl:
                infl[i] -= 1
        del infl[min(cand)[2]]
        cand.remove(min(cand))
        if len(cand) == 0:
            return set(infl.keys())



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
