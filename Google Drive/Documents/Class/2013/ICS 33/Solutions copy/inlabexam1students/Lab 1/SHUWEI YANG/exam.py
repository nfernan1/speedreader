from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):            
    def reachable(dic,nodes):
            for i in dic[nodes]:
                if i in reach:return reach
                else:reach.add(i)
                try:
                    for k in dic[i]:
                        reachable(dic,k)
                except:return reach
            return reach
    def read_notes(file):     
        dic = defaultdict(set)
        for line in file.readlines():
            nodes = [i.strip() for i in line.split(';')]
            try:dic[nodes[0]].add(nodes[1])
            except:dic[nodes[0]] = nodes[1]
        return dict(dic)
    
    dic = read_notes(file)
    for c in dic:
        reach = set()
        dic[c].union(reach)
    return dic

def print_graph(graph):
    print('Graph: source nodes(ordered -> destination nodes(ordered))')
    for c in sorted(graph):
        text = ''
        for i in sorted(graph[c]):
            text += i+','
        print(c,'->',text)

def find_influencers(graph):
    infl = dict()
    for c in graph:
        infl[c] = ceil(len(graph[c])/2)
    cand = [(infl[c],len(graph[c]),c) for c in infl if infl[c] >= 0]
    while True:
        if len(cand) == 0:
            return {c for c in infl}
            break
        cand = [(infl[c],len(graph[c]),c) for c in infl if infl[c] >= 0]
        cand.remove(sorted(cand)[0])
        for c in infl: 
            if sorted(cand)[0][2] in graph[c]:
                infl[c] -= 1



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
