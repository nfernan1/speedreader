from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    dictionary={}
    for line in file:
        msg=line.strip().split(';')
        if msg[0] in dictionary.keys():
            dictionary[msg[0]].add(msg[1])
        else:
            dictionary[msg[0]]=set(msg[1])
        if msg[1] in dictionary.keys():
            dictionary[msg[1]].add(msg[0])  
        else:
            dictionary[msg[1]]=set(msg[0])
    return dictionary
        

def print_graph(graph):
    print('Graph:source nodes(ordered)-> destination nodes(ordered)')
    for node in sorted(graph.keys()):
        sorted_nodes=sorted(graph[node])
        print(node,'->',sorted_nodes)
    

def find_influencers(graph):
    infl={}
    num_friends=0
    cand=[]
    for key in graph.keys():
        for friend in graph[key]:
            num_friends=num_friends+1
            # counting hte number of friends the person has
        infl[key]=num_friends-ceil(num_friends/2)  
    for person in infl.keys():
        if infl[person]>0:
            cand.append((infl[person],num_friends,person))
    while cand!=[]:
        print('infl',infl)
        print('cand',cand)
        min_value=cand.pop(0)
        for item in min_value:
            if type(item)==int:
                friend_count=item
            if type(item)==str:
                del infl[item]
                print('removing',min_value,"as key from infl; decrementing friend's value")
                for key in graph.keys():
                    for value in graph[key]:
                        if value==item:
                            infl[key]=(friend_count-1)-ceil((friend_count-1)/2)                          
    influencers=set(infl.keys())
    return influencers
         
        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
