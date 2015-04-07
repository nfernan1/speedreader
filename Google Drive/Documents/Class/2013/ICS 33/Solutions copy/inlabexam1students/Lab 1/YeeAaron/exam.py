from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.
# C:\Users\ics33-mtest1\Desktop\EclipseWorkspacePython\YeeAaron\graph.txt
def read_graph(file):
    temp = file.readlines()
    returndict = dict()
    for x in temp:
        new = x.split(";")
        first = new[0] #this is a string
        if '\n' in new[1]:
            second = new[1][:-1]
        else:
            second = new[1]
        if first not in returndict.keys():
            returndict[first] = set()
        if second not in returndict.keys():
            returndict[second] = set()
        returndict[first].add(second)
        returndict[second].add(first)
    return returndict

def print_graph(graph):
    keys = sorted(graph.keys())
    print ("Graph: source nodes (ordered) -> destination nodes (ordered)\n")
    for i in keys:
        destinations = ''
        for x in sorted(graph[i]):
            destinations += x+','
        print ("{} -> {}".format(i,destinations[:-1]))

def find_influencers(graph):
    infl = dict()
    for i in graph.keys():
        infl[i] = len(graph[i]) - ceil(len(graph[i])/2)
    cand = []
    for i in graph.keys():
        cand.append((infl[i],len(graph[i]),i))
    
    while len(cand) != 0:
        currentmin = min(infl.values())
        temp = ''
        for i in graph.keys():
            if infl[i] == currentmin:
                temp = i
                break
        friend_list = []
        for friend in graph[temp]:
            friend_list.append(friend)
        for x in friend_list:
            infl[x] -= 1
        #remove temp from canidate list
        #return remaining from infl
     
        

# C:\Users\ics33-mtest1\Desktop\EclipseWorkspacePython\YeeAaron\graph.txt

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    #print('Influencers =', find_influencers(graph))
