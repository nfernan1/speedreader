from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        x,y = line.strip('\n').split(';')
        graph[x].add(y)
        if y in graph[x]:
            graph[y].add(x)
    return graph
        
def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for key,value in sorted(graph.items()):
        print(key + ' -> ' + ' '.join(str(value)))
        
def find_influencers(graph):
    infl, cand = dict(), list()
    for key,value in graph.items():
        infl[key] = len(value) - ceil(len(value)/2)
    for key in graph.keys():
        if infl[key] >= 0:
            temp = tuple((infl[key], len(graph[key]), key))
            cand.append(temp)
    while len(infl) > 0:
        for entry in cand:
            if cand.count(entry[0]) > 1:
                pass
            elif cand.count(entry[1]) > 1:
                pass
            else:
                x = entry[2]
                del infl[x]
                for value in graph[x]:
                    infl[value] -= 1
        return infl
    
              
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
