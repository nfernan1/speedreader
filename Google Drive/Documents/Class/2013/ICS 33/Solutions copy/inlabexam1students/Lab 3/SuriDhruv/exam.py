from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
import math

# Define your functions here.

def read_graph(f):
        my_dict = defaultdict(set)
        my_list = []
        line = f.readlines()
        for f in line: 
            my_list = list(f.strip().split(";"))
            my_dict[my_list[0]].add(my_list[1])
            my_dict[my_list[1]].add(my_list[0])
        return(dict(my_dict))
        

def print_graph(graph):
    print("Graph: Source nodes (Ordered) -> Destination Nodes (ordered)")
    for i,j in sorted(graph.items()):
        print(i, "->",sorted(j))
        
        

def find_influencers(graph):
   
        infl = {}
        num = 0
        cand = []
    
        
        for i,j in graph.items():
            num = len(j)
            value = num - math.ceil(num/2)
            infl.update({i:value})
        for l,m in infl.items():
            cand.append((m,len(graph[l]),l))   
        print("old",infl)
        
        for q in range(7):
            for i in range(len(cand)-1):
                temp = 0
                if cand[i]<cand[i+1]:
                    temp = cand[i+1]
                    cand[i+1] = cand[i]
                    cand[i] = temp
            min = cand[-1]
            cand.pop(-1)
            for i,j in infl.items():
                if i != min[2]:
                    infl.pop(min[2])
                break
            print(graph[min[2]])
  
            print("new",infl)
        
            
           
        

        #print(new_list)
















# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                  'Could not find that file'))
    print(graph)
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
