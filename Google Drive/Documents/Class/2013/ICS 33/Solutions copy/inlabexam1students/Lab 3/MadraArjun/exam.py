from goody       import safe_open
import math   
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    d = dict()
    file = file.readlines()
    #print(file)
    
    for x in file:
        #print(x)
        strip_line = x.strip('\n')
        #print(strip_line)
        split_line = strip_line.split(';') 
        #print(split_line)
   
        
        d[split_line[0]]=set(split_line[1:])
        #print(d[split_line[0]])
        
        
        
        key  =  d[split_line[0]]
        
   

        value = split_line[1:]
    
#     print(value)
#     print(d[split_line[0]])
       
    print(d)
  
    
    
    
    return d
    

def print_graph(graph):
    
    for k in graph:
       print(k)
        
    print ('Graph: source nodes (ordered) -> destination nodes (ordered)',
          k, '->')

    

def find_influencers(graph):
   key = graph[0]
   value = graph[1:]
   num = len(value)
   operation = math.ceil(num/2)
   
   counter = 0
   
   for s in value:
       if '*' in s:
           counter +=1
   if counter >= operation:
       graph.pop(key)
       graph.add(key + '*')
       
       
    
   
  
  
        


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    
#     d = read_graph(graph)
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
  
