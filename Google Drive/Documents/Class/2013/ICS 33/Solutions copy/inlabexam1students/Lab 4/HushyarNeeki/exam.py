from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict
import math

# Define your functions here.
# Neeki Hushyar Lab 4

def read_graph(file):
    filename = file.readlines()
    list_of_pairs = []
    dictionary = dict()
    for i in filename:
        x = i.rstrip()
        list_of_pairs.append(x)
    newlist = []
    for i in list_of_pairs:
        x = i.split(';')
        newlist.append(x)

    for each_item in newlist:
        k = each_item[0]
        v = each_item[1]
        if k in dictionary.keys():
            dictionary[k].update(v)
        else:
            dictionary[k] = set(v)
    return dictionary

def print_graph(graph):
    list_keys = []
    for k in graph.keys():
        list_keys.append(k)
    for each in sorted(list_keys):
        print(each + ' -> ' + str(graph.get(each)))


def find_influencers(graph):
    influence = dict()
    candidate_list = []
    for k,v in graph.items():
        influence[k] = int(len(v)- math.ceil((len(v))/2))
        candidate_list.append(k)
    print('infl =', influence)
    
    
    while candidate_list != []:
        list_of_tup = []
        for key in influence.keys():
            if int(influence.get(key)) < 0:
                    candidate_list.remove(key)
        
            tup = (influence.get(key), len(graph.get(key)), key)
            list_of_tup.append(tup)
        print('cand =', list_of_tup)
        for i in range(len(list_of_tup)):
            minimum = list_of_tup[i][0]
            for each_tup in list_of_tup:
                if each_tup[0] < minimum:
                    minimum = each_tup[0]
        for i in range(len(list_of_tup)):
            newmin = each_tup[1]
            for each_tup in list_of_tup:
                
                if each_tup[0] == minimum:
                    if each_tup[1] < newmin:
                        newmin = each_tup[1]
                        
        for i in range(len(list_of_tup)):
            lastmin = each_tup[2] #letter?
            for each_tup in list_of_tup:
                if each_tup[0] == minimum and each_tup[1] == newmin:
                    if each_tup[2] < lastmin:
                        lasmin = each_tup[2]
                
        #remove proper candidate based on minimum count then delete break from the bottom
        #negative one candidates removed from friends list
    
             
        
        break  
    




# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
    
    
