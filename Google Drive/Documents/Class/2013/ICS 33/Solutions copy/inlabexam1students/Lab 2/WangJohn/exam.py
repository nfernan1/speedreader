from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    file=file.readlines()
    graph=defaultdict(set)
    for line in file:
        graph[line[0]].add(line[2])
        graph[line[2]].add(line[0])
    return dict(graph)

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes(ordered)')
    for person in sorted(graph):
        print('\t',person,' -> ',str(sorted(graph[person])).strip('[]'))

def find_influencers(graph):
    infl=defaultdict(int)
    for person in graph:
        infl[person]=len(graph[person])-ceil(len(graph[person])/2)
    while True:
        print('infl = ',dict(infl))
        cand=[]
        for person in infl:
            if infl[person]>-1:
                cand.append((infl[person],len(graph[person]),person))
        print('cand = ',sorted(cand))
        print('removing ',min(cand)[2]," as a key from infl; decrementing friend's values")
        del infl[min(cand)[2]]
        for person in infl:
            if min(cand)[2] in graph[person]:
                infl[person]-=1
        if cand==[]:
            break
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
