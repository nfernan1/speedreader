from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    quest = dict()
    list_file = list()
    txt = file.readlines()
    for item in txt:
        list_file.append(item.strip(';'))
    for item in list_file:
        key = list(quest.keys)
        if item[0] not in key:
            quest[item[0]] = set(item[1])
        else: 
            quest[item[0]] = quest[item[0]].union(set[item[1]])
        key = list(quest.keys())
        if item[1] not in key:
            quest[item[1]] = set(item[0])
        else:
            quest[item[1]] = quest[item[1]].union(set[item[0]])

    return quest
    
            
def print_graph(graph):
    key = sorted(graph)
    print('')
    for item in key:
            v = sorted(graph[item])
            v_str = '{}'.format(v[0])
            if len(v) == 1:
                for i in range(1,len(v[i])):
                    v_str += ', {}'.format(v[i])
            print('   {} -> {}'.format(i, v_str))


def find_influencers(graph):
    portal = []
    infl = dict()
    graph_k = sorted(graph.keys())
    
    while len(portal) != 0:
        for item in graph_k:
            value_l = ceil(len(graph[item])/2)
            infl[item] = len(graph[item]) - value_l
            portal.append(len(graph[item]) - value_l, len(graph[item]), item )
        mini_portal = []
        for item in portal:
            mini_portal.append(item[0])
        least = min(mini_portal)
        lost = []
        for item in portal:
            if least in item[0]:
                lost.append(item)
        
        if len(lost) > 1:
            mini_portal = []
            for item in lost:
                mini_portal.append(item[1])
            least = min(mini_portal)
            lost_1 = []
            for item in lost:
                if least in item[1]:
                    lost_1.append(item)
        
            if len(lost_1) > 1:
                mini_portal = []
                for item in lost_1:
                    mini_portal.append(item[1])
                least = min(mini_portal)
                lost_2 = []
                for item in lost_1:
                    if least in item[1]:
                        lost_2 = item
                portal.remove(lost_2)
                del infl[lost_2[2]]
            else:
                portal.remove(lost_1[0])
                del infl[lost_1[2]]
        else:
            portal.remove(lost[0])
            del infl[lost[2]]

    return(set(sorted(infl.keys())))
        
        
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
