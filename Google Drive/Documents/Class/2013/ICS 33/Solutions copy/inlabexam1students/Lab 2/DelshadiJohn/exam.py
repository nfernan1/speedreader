from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friends = defaultdict(set)
    for line in file:
        friends[line[0]].add(line[2])
        friends[line[2]].add(line[0])
    return friends

def print_graph(graph):
    print('Graph: source nodes(ordered) -> destination nodes (ordered)')
    for item in sorted(graph):
        print(item + '-> ' + str(list(graph[item])))

def find_influencers(graph):
    infl = defaultdict()
    for value in graph.keys():
        number_friends = len(graph[value])
        infl[value] = number_friends - ceil(number_friends/2)
    while True:
        cand = sorted([(infl[item],len(graph[item]),item) for item in infl.keys() if infl[item] >= 0])
        if len(cand) > 0:
#             for item in graph:
#                 if cand[0][2] in graph[item]:
#                     if infl[item] in infl:
#                         infl[item]= infl[value] -1
            del infl[cand[0][2]]   
            print(infl)     
        else:
            break
    

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
