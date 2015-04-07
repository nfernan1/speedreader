from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    newdict = defaultdict(set)
    for line in file:
        a,b = line.strip().split(';')
        newdict[a].add(b)
        newdict[b].add(a)
    return newdict

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for a,b in sorted(graph.items()):
        z = ','
        print(a,'->', z.join(sorted(b)))

def find_influencers(graph):
    tempgraph = graph.copy()
    infl = {c:0 for c in graph}
    for i in tempgraph.items():
        infl[i[0]]= len(i[1])- ceil(len(i[1])/2)
    cand = []
    temp = zip((infl.values()),graph.values(),(infl.keys()))
    for (a,b,c) in temp:
        cand.append((a,len(b),c))
    tempgraph = graph.copy()
    while cand:
        cand = sorted(cand)
        if cand[0][0] == 0:
            cand.remove(cand[0])
            infl[cand[0][2]] = infl[cand[0][2]]-1
            del infl[cand[0][2]] 
   
    

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
