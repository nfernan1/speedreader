from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file: 'file') -> dict:
    friends = dict()
    for lines in file:
        newlines = lines.strip().split(';')
        print('NL: ', newlines)
        if newlines[0] not in friends:
            friends[newlines[0]] = {newlines[1]}
#        elif newlines[1] not in friends:
#            friends[newlines[1]] = {newlines[0]}
        else:
            friends[newlines[0]].add(newlines[1])
    return(friends)
            
            
def print_graph(graph:dict) -> None:
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for friend in sorted(graph):
        print(' {} -> {}'.format(friend, graph[friend]))


def find_influencers(graph:dict) -> set:
    infl = dict()
    cand = []
    for items in graph:
        infl[items] = ((len(graph[items]))-(ceil(len(graph[items])/2)))
    for person in infl:
        while infl[person] >= 0:
            x=(set(zip(infl[person], len(graph[person]),person)))
            cand.append(x)
    return(cand)



# Script

if __name__ == '__main__':
#    graph = read_graph(safe_open('Enter name of file with graph', 'r',
#                                 'Could not find that file'))
    graph = {'i':{'j'}, 'h':{'g'}, 'j':{'i','g'}, 'a':{'c','b'}, 'c':{'a','b','d','g'},'b':{'a','c'}, 'e':{'d'}, 'd':{'c','e','f'}, 'g':{'h','c','j'}, 'f':{'d'}}
#    print_graph(graph)
    core = find_influencers(graph)
#    print('Influencers =', find_influencers(graph))
