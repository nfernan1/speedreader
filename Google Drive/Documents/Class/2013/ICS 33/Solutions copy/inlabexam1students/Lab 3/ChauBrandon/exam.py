from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    list1=[]
    dict1={}
    for x in file:
        if x[0] not in dict1.keys():
            dict1[x[0]]=set()
        for y in dict1.keys():
            for z in dict1.get(y):
                if x[0] == z:
                    dict1.get(x[0]).update(y)
        dict1.get(x[0]).update(x[2])
    for k in dict1.keys():
        for h in dict1.get(k):
            if h not in dict1.keys():
                list1.append(tuple([h,k]))
    for x in list1:
        if x[0] not in dict1.keys():
            dict1[x[0]]=set()
        dict1.get(x[0]).update(x[1])
    return dict1

def print_graph(graph):
    print ("Graph: source nodes (ordered) -> destination nodes (ordered)")
    for x in sorted(graph):
        str1 = ", ".join(sorted(graph.get(x)))
        print ("  {} -> {}".format(x,str1))
        
        
def find_influencers(graph):
    infl={}
    cand=[]
    for x in graph.keys():
        num_of_friends = len(graph.get(x))
        infl[x] = num_of_friends - ceil(num_of_friends/2)
        cand.append(tuple([infl.get(x),num_of_friends,x]))
    print (cand)
    while len(cand) != 0:
        cand_to_remove = min(cand)
        friends = list(graph.get(cand_to_remove[2]))
        for x in friends:
            if x in infl.keys():
                infl[x] = infl.get(x)-1
#                for u in cand:
#                    if x == u[2]:
        infl.pop(cand_to_remove[2])
        cand.remove(cand_to_remove)
    return infl
            
        
        
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
