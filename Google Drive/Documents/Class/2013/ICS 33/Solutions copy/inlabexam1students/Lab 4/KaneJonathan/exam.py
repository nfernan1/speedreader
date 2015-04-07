from goody       import safe_open
from goody       import leading
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict



# Define your functions here.

def read_graph(file):
    #mental breakdown
    data = file.readlines()
    dictionary = defaultdict()
    data = [node.replace('\n','') for node in data]
    for node in data:
        if node[0] not in dictionary.keys():
            dictionary.update({node[0] : set(node[-1])})
        else:
            dictionary.update({node : set(node[-1])}) #confused
    return dictionary

def print_graph(graph):
    print('Graph: Source nodes (ordered) -> destination nodes (ordered)')
    for k, v in graph.items():
        print(k, ' -> ', v)

def find_influencers(graph):
    infl = [dict(k , len(v) - math.ceil(len(v)/2)) for k, v in graph]
    cand = []
    cand.append(k)
    


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
