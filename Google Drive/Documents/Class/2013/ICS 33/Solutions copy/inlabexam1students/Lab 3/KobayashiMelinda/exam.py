from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    print('Starting read_graph:::\n')
    lines = file.readlines()
    print(lines)
    lines = [i.strip('\n') for i in lines]
    print(lines)
    dict_friends = defaultdict(set)
    for line in lines:
        dict_friends[line[0]].add(line[2])
        dict_friends[line[2]].add(line[0])
        
    print('Final dict_friends is: ', dict_friends)
    print()
    print('End read_graph...\n\n')
    return dict_friends
            
    
def print_graph(graph):
    print('Starting print_graph:::\n')
    print('Graph: source nodes (ordered) -> destination nodes '
          '(ordered)')
    for key, value in sorted(graph.items()):
        value = sorted(value)
        empty_string = ' '
        print(' {} -> {}'.format(key, empty_string.join(value)))
    print('End print_graph...\n\n')

def find_influencers(graph):
    print('Starting find_influencers:::\n')
    infl = defaultdict(int)
    for key, value in graph.items():
        infl[key] += ceil(len(value)/2)
    print('infl dict is: ', infl)
    print()
    while True:
        cand = []
        for key, value in infl.items():
            if value >= 0:
                cand.append((value, len(graph[key]), key))
        print('cand list: ', cand)
        sorted(cand)
        print(cand)
        break



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
