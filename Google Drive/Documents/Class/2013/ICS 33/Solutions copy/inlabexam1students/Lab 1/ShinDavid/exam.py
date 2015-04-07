#David Shin
#lab 1
#54513301


from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict

import math

# Define your functions here.

def read_graph(file:'file object'):
    '''Takes a open file as an argument and reads that file, stores the graph as any kind of dictionary in the standard way. '''
    friend_dict = {}
    friend_list = []
    for i in file: #i is of str type. i is in the form 'a;b\n'
        k = i.strip('\n').split(';')
        friend_list.append(k)
        friend_dict[k[0]] = k[1]
        
    print(friend_dict,'fd')
    print(friend_list,'fl')
    
    return friend_dict
    
#     friend_dict[k[0]] = k[1]
        
#         friend_dict[friend_list[0]] = friend_list[1] 
      
#         friend_list = i.split(';')
 

   
    
    
def print_graph(graph:dict):
    ''' '''
    print('\n\n')
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    print('\n')
    for i in graph.keys():
        print("{} -> {}".format(i,graph[i]))
    print('\n')


def find_influencers(graph:dict): 
    '''Passes in the {person:friends} dictionary and returns a core group of friends.'''
    influ = {} #keys are every node name.
    cand = []
    for j in graph.keys():
        for i in graph.values():
            influ[j]= i- math.ceil(i/2)
       
        
        print(influ,'influ')
        
        for key in influ.keys(): #Placing all influ values to the list cand
                if influ[key] >0:
                    cand.append((influ[key],graph[key],key))
            
        print(cand,'cand')    
        
#     while len(cand)>0:
        min_list = []
        for tuple in cand:
            if tuple[0] == 0:
                min_list.append(tuple)
#         
#         
#     
            
            

            


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    graph = {'h':3,'j':5,'d':1,'e':6,'f':3,'a':4,'c':2}
    find_influencers(graph)
#     core = find_influencers(graph)
#     print('Influencers =', find_influencers(graph))
#     
#     
#     
#EOF
