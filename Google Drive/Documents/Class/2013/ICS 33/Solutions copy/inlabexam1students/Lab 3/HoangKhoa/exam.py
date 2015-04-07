from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    lst = file.readlines()
    pretty_lst = []
    d = {}
    file.close()

    for e in lst:
        pretty_lst.append(e.strip())

    for i in range(len(pretty_lst)):
        d[pretty_lst[i][0]] = set()
        d[pretty_lst[i][2]] = set()
    
    for i in range(len(pretty_lst)):
        d[pretty_lst[i][0]].add(pretty_lst[i][2])
        d[pretty_lst[i][2]].add(pretty_lst[i][0])
    
    return d
    

def print_graph(graph):
    print("Graph: source nodes (ordered) -> destination nodes (ordered)")
    for (k, v) in sorted(graph.items()):
        lst = list(v)
        lst.sort()
        s = ""
        for char in lst:
            s += ", " + char
        print(k, "->", s[1:]) #Note that v is a set

def find_influencers(graph):
    infl = {k: (len(graph[k]) - ceil(len(graph[k])/2)) for k in graph} #keys are every node name in the graph
    cand = [(infl[k], len(graph[k]), k) for k in infl]
    print("infl", infl)
    print("cand", cand)
    g = 0
    while g < 10:
        #num_lst = []
        #neg_count = 0
        for i in range(1, len(cand)):
            print(cand[i-1], "<", cand[i])
            if cand[i-1] < cand[i]:   #cand[i] is a tuple
                try:
                    del(infl[cand[i-1][2]])
                    infl[cand[i-1][2]] -= 1
                    print(infl)
                except:
                    continue
        g+=1
#             for k in infl:
#                 num_lst.append(infl[k])
#             for n in num_lst:
#                 if n < 0:
#                     neg_count += 1
#             if neg_count == 0:
#                 break
            #infl[cand[i][2]] -= 1



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
