from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    new_fil = defaultdict(set)
    read = open(file)
    for i in read.readlines():
        new_value = i.strip('\n').split(';')
        
        new_fil[new_value[0]].add(new_value[1])
        new_fil[new_value[1]].add(new_value[0])
        
    return new_fil
a = read_graph('graph.txt')
print(a)
def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered')
    order_graph = sorted(graph)
    for i in order_graph:
        print(i, ' -> ', str(sorted(graph[i])).strip('[]'))
        
print_graph(a)
def find_influencers(graph):
    infl = dict()
    cand = []
    for i in graph:
        friends = (len(graph[i])/2)
        infl[i] = ceil(friends)
    for i in infl:
        if infl[i] >-1:
            cand.append((infl[i],len(graph[i]),i))
    return cand
        
       
    
print(find_influencers(a))


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
