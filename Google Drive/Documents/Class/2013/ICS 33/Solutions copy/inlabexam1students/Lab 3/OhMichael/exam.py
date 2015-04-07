from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    content, graph_dict = file.readlines() , {}
    for line in content:
        if line.endswith('\n'):
            line = line[:-1].split(';')
            if line[0] not in graph_dict: graph_dict[line[0]] = {line[1]}
            else: graph_dict[line[0]] = {line[1]}
        else:
            line = line.split(';')
    return graph_dict
    pass

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for item in sorted(graph.items()):
        print(' ', item[0], '->', item[1])
    pass

def find_influencers(graph):
    infl, cand = {}, []
    for item in graph.items():
        for k in item[0]: infl[k] = (len(graph.get(k)) - ceil((len(graph.get(k))/2)))
    for x in infl.keys():
        z = infl.get(x)
        y = len(graph.get(x))
        cand.append((z,y,x))
    
#     while True:
#         if cand != []:

#             pass
#         else:
#             return 
#             break
    pass



# Script

if __name__ == '__main__':
#     graph = read_graph(safe_open('Enter name of file with graph', 'r',
#                                  'Could not find that file'))
    graph = {'i': {'j'}, 'h':{'g'}, 'j':{'i','g'}, 'a': {'c','b'}, 'c':{'a','b','d','g'}, 'b':{'a','c'}, 'e':{'d'}, 'd':{'c','e','f'}, 'g':{'h','c','j'}, 'f':{'d'}}
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
