# CIARRA ALTOVEROS, LAB 3, ID: 33218028
from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friend_dict= defaultdict(set)
    for line in file.readlines():
        line= line.strip().split(';')
        friend_dict[line[0]].add(line[1])
        friend_dict[line[1]].add(line[0])
    return dict(friend_dict)



def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for k, v in sorted(graph.items()):
        v_list = list(v)
        v_list.sort()
        print("  {} -> {}".format(k, ', '.join(v_list)))
        
        

def find_influencers(graph):
    infl, cand = {}, []
    
    for k, v in graph.items():
        infl[k] =  len(v) -  ceil(len(v)/2)
        cand.append((infl[k], len(graph[k]), k))
    
    while len(cand) > 1 :
        for item in cand:
            if infl[item[-1]] < 0:
                cand.pop(cand.index(item))  
            if cand.count(item[0]) >1:
                if cand.count(item[1])>1:
                    cand.sort(key= item[2])
                elif cand.count(item[1])==1:
                    cand.sort(key= item[1])
            else:
                cand.sort()
                
        for friend in graph[cand[0][-1]]:
            if friend in infl.keys():
                infl[friend] -= 1
        
        del infl[cand[0][-1]] 
        cand.pop(0)
   
    return set(infl.keys())

        


#Script
if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
