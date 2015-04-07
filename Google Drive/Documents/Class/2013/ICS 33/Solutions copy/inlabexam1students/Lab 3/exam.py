#================================#
#    Michelle Lim ID 52485526    #
#    Lab #3 : 22 October 2013    #
#================================#
from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
# Define your functions here.
def read_graph(file):
    d = defaultdict()
    for line in file.readlines():
        l = line.strip('\n').split(';')
        if l[0] not in d : d.setdefault(l[0],{l[1],})
        if l[1] not in d : d.setdefault(l[1],{l[0],})
        if l[0] in d : d[l[0]].add(l[1])
        if l[1] in d : d[l[1]].add(l[0])
    return dict(d)     

def print_graph(graph):
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for key,val in sorted(zip([k for k in graph.keys()],[v for v in graph.values()])) : print ('   ',str(key), ' -> ', ', '.join(sorted([node for node in val])))

def find_influencers(graph):
    # returns a set containing the influencing nodes 
    infl = {}
    for key in graph : infl[key]=len(graph[key])-(ceil(len(graph[key])/2))
#         print (key, len(graph[key])-(ceil(len(graph[key])/2)))
#     print(infl)

    while 0 not in infl.values() or -1 not in infl.values():
        cand = []
        for key in infl : cand.append((infl[key],len(graph[key]),key))
        cand = sorted(cand)
        del infl[cand[0][2]]
        for key in graph : 
            if cand[0][2] in graph[key] : 
                infl[key] -= 1
        print('infl = ', infl)
        print('cand = ', cand) 
#         break
    return {key for key in infl.keys()}
    
# Could not figure out while loop! ): 10-15 more minutes would have done it. 
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))

