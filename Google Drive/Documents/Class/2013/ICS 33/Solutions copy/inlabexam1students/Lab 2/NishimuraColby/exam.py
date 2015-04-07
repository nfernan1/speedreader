from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    diction = defaultdict(set)
    temp = file.readlines()
    for i in range(len(temp)):
        temp[i] = temp[i].strip('\n')
        temp[i] = temp[i].split(sep=';')
    for i in temp:
        diction[i[0]].add(i[1])
        diction[i[1]].add(i[0])
    return dict(diction)
    

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    temp = sorted(list(graph.keys()), key= str.lower)
    for i in temp:
        print('  {0} -> {1}'.format(i, ', '.join(sorted(list(graph[i]), key = str.lower))))
    print('')

def find_influencers(graph):
    temp = list(graph.keys())
    infl = dict()
    for i in temp:
        infl[i] = len(graph[i]) - ceil((len(graph[i])/2))
    while True:
        cand = []
        for i in list(infl.keys()):
            if infl[i] > -1:
                cand.append((infl[i], len(graph[i]), i))
        if cand == []:
            return set(infl.keys())
        else:
            mini = min(cand)
            for i in graph[mini[2]]:
                try:
                    infl[i] -= 1
                except KeyError:
                    pass
            infl.pop(mini[2])
            
            



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
