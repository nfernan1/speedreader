from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friendship = defaultdict(set)
    for line in file.readlines():
        s,d = line.strip().split(';')
        friendship[s].add(d)
        friendship[d].add(s)
    return dict(friendship)

def print_graph(graph):
    print('Graph: source node(ordered) -> destination nodes(ordered)')
    fri = ', '
    for k,v in sorted(graph.items()):
        print(' ',k,'->',fri.join(sorted(list(v))))

def find_influencers(graph):
    infl = dict()
    for k,v in graph.items():
        infl[k] = len(tuple(v))-ceil(len(tuple(v))/2)
    while True:
        cand = [(infl[i],len(graph[i]),i) for i in infl.keys() if infl[i]>=0]
        if cand == []:
            return set(infl.keys())
        com = cand[0]
        for i in cand[1:]:
            if i[0]<com[0] or (i[0] == com[0] and i[1]<com[1]) or (i[0] == com[0] and i[1] == com[1] and i[2]<com[2]):
                com = tuple(i)
        infl.pop(com[2])
        for k,v in infl.items():
            if com[2] in graph[k]:
                infl[k] = v-1       



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
