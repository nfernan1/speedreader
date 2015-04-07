from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    f = file.readlines()
    mydict = defaultdict(set)
    for lines in f:
        newlist = list(lines.strip( ).split(';'))
        mydict[newlist[0]].add(newlist[1])
    return dict(mydict)
        
def print_graph(graph):
    print ('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for k,v in sorted(graph.items()):
        print(k,'->',' ',sorted(v))
        

def find_influencers(graph):
    keylist = []
    valuelist = []
    cand = []
    influencers= set()
    for k in graph.keys():
        keylist.append(k)
    for v in graph.values():
        valuelist.append(ceil(len(v)/2))
    infl = dict(zip(keylist,valuelist))
    for k,v in infl.items():
        if v>0:
            item = (v,len(graph[k]),k)
            cand.append(item)
        for k in infl.keys():
            for item in cand:
                if item[0] == min: 
                    infl.pop(item)
                    influencers.update(k)
    return influencers 
            
        


    
    


        
    
    
    



# Script
if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))

    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
