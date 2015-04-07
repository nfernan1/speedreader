from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friend_file = file.readlines()
    friendship_dict = defaultdict(set)
    for line in friend_file:
        new_line = line.strip('\n')
        friendship = new_line.split(';')
        friend_1, friend_2 = friendship[0], friendship[1]
        friendship_dict[friend_1].add(friend_2)
        friendship_dict[friend_2].add(friend_1)
    return dict(friendship_dict)
        
def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    sorted_friends = sorted(graph)
    for friend in sorted_friends:
        sorted_f = sorted(graph[friend])
        to_print = ''
        for i in range(len(sorted_f)):
            if i == (len(sorted_f) - 1):
                to_print += sorted_f[i]
            else:
                to_print += sorted_f[i]
                to_print += ', '
        print('    ' + friend + ' -> ' + to_print)

def find_influencers(graph):
    influence = dict()
    for key in list(graph.keys()):
        friends = len(list(graph[key]))
        half = ceil(friends/2)
        value = friends - half
        influence[key] = value
    x = 1
    while x != 0:
        candidates = []
        for key in list(influence.keys()):
            if influence[key] < 0:
                pass
            else:
                candidates.append((influence[key], len(list(graph[key])), key))
        x = len(candidates)
        minimum = min(candidates)
        to_remove = minimum[2]
        del influence[to_remove]
        for key in list(influence.keys()):
            friends = list(graph[key])
            f = len(friends)
            if to_remove in friends:
                f = len(friends) - 1
            half = ceil(f/2)
            value = f - half
            influence[key] = value
        

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
