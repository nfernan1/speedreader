from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict

# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        s, d = line.strip().split(';')
        graph[s].add(d)
    return graph

def print_graph(graph):
    print('Graph: source nodes(ordered) -> destination nodes(ordered)')
    for s, d in sorted(graph.items()):
        print('{} -> {}'.format(s, d))

def find_influencers(graph):
    infl = dict()
    for key in graph.keys():
        values = graph[key]
#         print(values)
        number_of_friends = len(values)- (math.ceil(len(values))/2)
        infl.update(values)
        infl.update(number_of_friends)
        candidate = []
        candidate.append((infl[0],len(values), key))
        for friends in candidate:
            candidate.pop(min(friends[1]))  
            print("removing {} as key from infl; decrementing friend's values".format(friends[2]))
            
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
