from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.
def read_graph(file):
    f = defaultdict(set)
    for line in file.readlines():
        f[line[0]].add(line[2])
        #for i in f.items:
        #    if i in 

           
    print(f)

        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for key, value in graph.items():
      print('{} -> {}').format((key, value).sort())     


def find_influencers(graph):
    infl = {}
    keys = []
    values = []
    for k in graph.keys():
        keys.append(k)
    for v in graph.keys():
        y = len(graph.values())- len(.5*(graph.values()))
        x = math.ceil(y)
        values.append(x)
        
    infl[keys]= values 
    
    while len(infl > 0):
        cand = []
        for i in values:
            if i in values > 0:
                cand.append((i, len(graph.values(), graph.keys())))
                
    mini = min(cand[0])
    cand.remove(mini)
    
            
    
           
    
    



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
