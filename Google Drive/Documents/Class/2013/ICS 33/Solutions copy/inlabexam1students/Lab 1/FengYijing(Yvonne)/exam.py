from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    '''given a file containing a graph returns a dict[name] = set(names)'''
    friendship_dict = defaultdict(set)
    graph_info = file.readlines()
    for line in graph_info:
        each_friend = line.strip().split(';')
        friendship_dict[each_friend[0]].add(each_friend[1])
        friendship_dict[each_friend[1]].add(each_friend[0])
    return dict(friendship_dict)

    

def print_graph(graph):
    '''given the graph input(which represents the friendship_dict)'''
    '''prints out the names in alph order with friends in alph order'''
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for name_key in sorted(graph.keys()):
        friendship_info = ', '.join(sorted(list(graph[name_key])))
        # gets all the friendship for one person(name_key)
        print('  {} -> {}'.format(name_key, friendship_info))
    print()


def find_influencers(graph):
    '''given the graph dict returns the set of nodes that '''
    '''can influence everyone in the graph'''
    infl = {}
    for name_key in graph.keys():
        value_of_friends = len(graph[name_key])
        # count how many friends this person(name_key) has
        infl[name_key] = value_of_friends - ceil(value_of_friends / 2)
    cand = [(infl[each_name], len(graph[each_name]), each_name)  for each_name in infl.keys()]
    # cand = [(infl_value, how_many_friends, name_of_this_person)]
    while cand != [] and sorted(cand)[-1][0] >= 0:
        minum_influence = sorted(cand)[0][2]
        del infl[minum_influence]
        for name_key in graph.keys():
            if name_key in infl.keys() and minum_influence in graph[name_key]:
                infl[name_key] -= 1
        cand = [(infl[each_name], len(graph[each_name]), each_name)  for each_name in infl.keys() if infl[each_name] >= 0 ]
    return set(infl.keys())
        
        


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
