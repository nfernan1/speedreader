from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
import copy

# Define your functions here.

def read_graph(file):
    result = {}
    for line in file:
        for i in line.strip('\n').split(';'):
            copyls = copy.copy(line.strip('\n').split(';'))
            copyls.remove(i)
            other = copyls[0]
            if i not in result:
                result[i] = {other}
            elif i in result:
                result[i].add(other)
    return result

def print_graph(graph):
    print("Graph: source nodes (ordered) -> destination nodes (ordered)")
    for i in sorted(graph.items()):
        a = ''
        for k in sorted(i[1]):
            a = a + k + ','
        print(i[0],'->',a.strip(','))

def find_influencers(graph):
    a = copy.copy(graph)
    while True:
        infl = {}
        for i in a.keys():
            count = 0
            for r in a[i]:
                if r != 'ok':
                    count += 1
            infl[i] = count - ceil(len(a[i])/2)
        cand = []
        for k in infl:cand.append((infl[k],len(a[i]),k))
        cand.sort()
        if cand[0][2] in a:
            a.pop(cand[0][2])
        for l in a.values():
            if cand[0][2] in l:
                l.remove(cand[0][2]) 
                l.add('ok')
        if max(list(infl.values())) < 0:
            break
    return infl.keys()


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
