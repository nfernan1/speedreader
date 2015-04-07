from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    result = dict()
    file_list = []
    txt_file = file.readlines()
    for i in txt_file:
        file_list.append(i.strip().split(';'))
    print(file_list)
    
    for i in file_list:
        keys = list(result.keys())
        if i[0] not in keys:
            result[i[0]] = set(i[1])
        else:
            result[i[0]] = result[i[0]].union(set(i[1]))
        keys = list(result.keys())
        if i[1] not in keys:
            result[i[1]] = set(i[0])
        else:
            result[i[1]] = result[i[1]].union(set(i[0]))
    return result

def print_graph(graph):
    keys = sorted(graph)
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for i in keys:
        value = sorted(graph[i])
        value_str = '{}'.format(value[0])
        if len(value) > 1:
            for j in range(1,len(value)):
                value_str += ', {}'.format(value[j])
        print('  {} -> {}'.format(i, value_str))

def find_influencers(graph):
    loop = True
    influ = dict()
    cand = []
    while loop:
        influ = dict()
        cand = []

        graph_keys = sorted(graph.keys())
        for i in graph_keys:
            len_value = ceil(len(graph[i])/2)
            influ[i] = len(graph[i]) - len_value
            cand.append((len(graph[i]) - len_value, len(graph[i]), i))

            
        min_cand = []
        for i in cand:
            min_cand.append(i[0])
        smallest = min(min_cand)
        kicked = []
        for i in cand:
            if smallest == i[0]:
                kicked.append(i)
        
        if len(kicked) > 1:
            min_cand = []
            for i in kicked:
                min_cand.append(i[1])
            smallest = min(min_cand)
            kicked2 = []
            for i in kicked:
                if smallest == i[1]:
                    kicked2.append(i)
           
            if len(kicked2) > 1:
                min_cand = []
                for i in kicked2:
                    min_cand.append(i[1])
                smallest = min(min_cand)
                for i in kicked2:
                    if smallest == i[1]:
                        kicked3 = i
                cand.remove(kicked3)
                del graph[kicked3[2]]
            else:
                cand.remove(kicked2[0])
                del graph[kicked2[2]]
        else:
            cand.remove(kicked[0])
            del graph[kicked[2]]
        if len(cand) == 0:
            loop = False
            
    return set(sorted(influ.keys()))
        
                
            


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)

    print('Influencers =', find_influencers(graph))
