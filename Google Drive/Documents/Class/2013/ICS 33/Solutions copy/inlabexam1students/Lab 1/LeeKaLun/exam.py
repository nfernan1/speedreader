from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    d = dict()
    infile = open(file,'r')
    read_line = infile.readline().strip()
    while read_line:
        read_line = read_line.strip()
        read_line = read_line.split(';')
        key,value = read_line
        read_line = infile.readline().strip()
        if key in d:
            d[key].add(value)
        else:
            if key not in d:
                d[key] = {value}
    return d  
        
    

def print_graph(graph):
    print('Graph: source nodes(ordered) -> destination nodes (ordered)')
    keys = sorted(graph.keys())
    for key in keys:
        for i in range(len(graph[key])):
            a = ''
            for value in graph[key]:
                if len(a) == 0:
                    a += value + ','
                else:
                    a += value
             
        print(key,'->',a)

def find_influencers(graph):
    infl = dict()
    keys = graph.keys()
    cand = list()
    for key in keys:
        infl[key] = len(graph[key]) - ceil(len(graph[key])/2)
    
    for key in infl.keys():
        if infl[key] >= 0: 
            cand.append((infl[key],len(graph[key]),key))    
    print('infl:',infl)
    print('cand:',cand)        



# Script

if __name__ == '__main__':
    a = read_graph('graph.txt')
    print_graph(a)
    find_influencers(a)
#     graph = read_graph(safe_open('Enter name of file with graph', 'r',
#                                  'Could not find that file'))
#     print_graph(graph)
#     core = find_influencers(graph)
#     print('Influencers =', find_influencers(graph))
