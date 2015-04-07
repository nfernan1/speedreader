from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    dic = dict()
    lines = file.readlines()
    for line in lines:
        if line[0] not in dic.keys():
            dic[line[0]] = {line[2]}
        else:
            dic[line[0]].add(line[2])
            
        if line[2] not in dic.keys():
            dic[line[2]] = {line[0]}
        else:
            dic[line[2]].add(line[0])
            
    print (dic) #comment this out later
    return dic
            

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for k, v in sorted(graph.items()):
        print('{} -> {}'.format(k,sorted(v)))

def find_influencers(graph):
    infl = dict()
    for k,v in graph.items():
        infl[k] = len(v) - ceil(len(v)/2)
    print(infl)
    
    cand = []
    for k,v in infl.items():
        if v < 0:
            pass
        else:
            cand.append((v,len(graph[k]), k))
    
    while cand != []:
        take_out = (min(cand))
        cand.remove(take_out)
        
        print(take_out[2])                  #smallest one
        del infl[take_out[2]]               #deletes item from infl
        
        
        node = take_out[2]  
        for key, v in graph.items(): 
            if node in v:
                infl[key] = infl[key] - 1   # decrements
        
        print('infl' , infl)
    
        
    newset = set()
    for item in cand:
        newset.add(item)

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
