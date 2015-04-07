from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    new_dict = dict()
    infile = file.readlines()
    for line in infile:
        line.strip()
        if line[0] not in new_dict :
            new_dict[line[0]] = set(line[2])
            for line in infile:
                if line[2] not in new_dict:
                    new_dict[line[2]] = set(line[0])
                else:
                    new_dict[line[2]].add(line[0])    
        else:
            new_dict[line[0]].add(line[2])           
    return new_dict

def print_graph(graph):
    print()
    print('Graph : source nodes (ordered) -> destination nodes (ordered)')
    for k,v in sorted(graph.items()):
        print(k, '->', v )

def find_influencers(graph):
    infl = dict()
    cand = []
    for key,value in sorted(graph.items()):
        new_value = len(value) - ceil( ( len(value)/2 ) )
        infl[key] = new_value
    
        
    for key,value in sorted(graph.items()):
        new_value = len(value) - ceil( ( len(value)/2 ) )    
        tuple = (new_value, len(value), key)
        cand.append(tuple)
        
    print( 'infl =', infl)
    print('cand =',cand)
    
    
        
        
        
        
       
        
            
        
    

       
        
        
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
