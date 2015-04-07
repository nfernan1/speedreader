from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    local_dd = defaultdict(list)
    node_dict = {}
    for line in file.readlines():
        local_dd[line.strip().split(';')[0]].append(line.strip().split(';')[-1])
        local_dd[line.strip().split(';')[-1]].append(line.strip().split(';')[0])
    for item in local_dd:
        node_dict[item]=set(local_dd[item])
    #print(node_dict)
    return node_dict

def print_graph(graph):
    
    print('Graph: source nodes (ordered) -> destination nodes (ordered) ')
    for k in sorted(graph):
        value = ''
        for v in sorted(graph[k]):
            value += v+', ' 
        print('  %s -> %s' % (k, value))

def find_influencers(graph):
    #1
    infl={}
    for node in graph:
        infl[node] = len(graph[node])-ceil(len(graph[node])/2)
    #2
    while True:
        cand=[]
        for key in infl.keys():
            if infl[key] >= 0:
                cand.append((infl[key], len(graph[key]), key))
            else:
                pass
        if len(cand) == 0:
            break
#         print('%s = %s' % ('infl', infl))
#         print('%s = %s' % ('cand', cand))
        pop_val = sorted(cand)[0]
#         print('removing %s as key from infl; decrementing friend"s values' % pop_val[-1])
#         print(cand.index(pop_val))
#         print('deleting item: {}'.format(cand[cand.index(pop_val)]))
        cand.pop(cand.index(pop_val))
        del infl[pop_val[-1]]
        for key in infl:
            if pop_val[-1] in graph[key]:
                 infl[key] -= 1
#         print('-----end-----')
    final = set()
    for key in infl.keys():
        final.add(key)
    return final

#     cand=[]
#     for key in infl.keys():
#         if infl[key] >= 0:
#             cand.append((infl[key], len(graph[key]), key))
#     pop_val = sorted(cand)[0]
#     cand.pop(cand.index(sorted(cand)[0]))
#     
#     del infl[pop_val[-1]]
#     print(cand)
#     print(infl)

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file', default='graph.txt'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
