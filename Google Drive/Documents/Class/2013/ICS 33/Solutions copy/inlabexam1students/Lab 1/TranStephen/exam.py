from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph=defaultdict(set)
    for line in file:
        new_line=line.strip().split(';')
        graph[new_line[0]].add(new_line[-1])
        graph[new_line[-1]].add(new_line[0])
    return dict(graph)
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for node in sorted(graph):
        print('  {} -> {}'.format(node,', '.join(sorted(graph[node]))))
        
        
def find_influencers(graph):
    infl=dict()
    for element in graph:
            infl[element]=(len(graph[element])-ceil(len(graph[element])/2))
    while (x for x in infl.values() if x < 0):
        cand=[]
        for element in infl:
            if infl[element]>=0:
                cand.append((infl[element],len(graph[element]),element))
        x=(min(cand))
        cand.remove(x)
        infl.pop(x[2])
        for n in graph[x[2]]:
            if n in infl:
                infl[n]-=1
        if len(cand)<0:
            break
    return infl



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file','graph.txt'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
