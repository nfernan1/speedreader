from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    file_dict = defaultdict(set)
    for line in file:
        a = line.strip().split(';')
        file_dict[a[0]].add(a[1])
    return dict(file_dict)



def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    tuples = graph.items()
    for m,n in sorted(tuples):
        print(m+' -> ', ', '.join(sorted(n)))
        

def find_influencers(graph):
    infl = dict()
    cand = []
    b = []
    for i in graph:
        infl[i] =len(graph[i]) - ceil((len(graph[i]) /2))
        a = (infl[i],len(graph[i]), i)
        cand.append(a)
    for m in sorted(cand):
        b.append(m)

        
    print(b)
        
    
    
    
    
    
    return infl



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
