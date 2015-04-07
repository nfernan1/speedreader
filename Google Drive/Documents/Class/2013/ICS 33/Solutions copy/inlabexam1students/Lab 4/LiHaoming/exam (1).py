from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    text1 = file.readlines()
    list1 = []
    for i in text1:
        i = i.replace('\n','')
        list1.append(i)
        list1.append(i[-1]+';'+i[0])
    dict1 = defaultdict(set)
    for i in list1:
        dict1[i[0]].add(i[-1])
    return dict1

def print_graph(graph):
    print('Graph: sourse nodes (ordered) -> destination nodes(ordered)')
    for i in sorted(graph.keys()):
        list1 = []
        for n in graph[i]:
            list1.append(n)
        list1.sort()
        print(' ',i,' -> ',', '.join(list1))

def find_influencers(graph):
    infl = dict()
    cand = []
    for i1 in graph:
        infl[i1] = len(graph[i1]) - ceil(len(graph[i1])/2)
    for i2 in infl:
        cand.append((infl[i2],len(graph[i2]),i2))
    while len(cand) > 0:
        min1 = min(cand)
        cand.remove(min1)
        del infl[min1[-1]]
        for i3 in infl:
            if min1[-1] in list(graph[i3]):
                infl[i3] -= 1
            elif infl[i3] < 0:
                try:
                    cand.remove((infl[i3],len(graph[i3]),i3))
                except:
                    pass
    return infl.keys()
                

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
