from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    myDict = {}
    myFile = file.read().splitlines()
    for line in myFile:
        value = line.split(';')
        myDict.setdefault(value[0],set(value[1])).add(value[1])
        myDict.setdefault(value[1],set(value[0])).add(value[0])
    return(myDict)

def print_graph(graph):
    print('Graph:  source nodes (ordered) -> destination nodes (ordered)')
    for i in sorted(graph):
        line = ', '.join(j for j in sorted(graph[i]))
        print('  {} -> {}'.format(i,line))

def find_influencers(graph):
    infl = {}
    cand = []
    go = True
    for person in graph:
        infl[person]= len(graph[person])-ceil(len(graph[person])/2)
    while go:
        cand = []
        for element in infl:
            if infl[element]>=0:
                cand.append((infl[element],len(graph[element]),element))
        print('infl = {}'.format(infl))
        print('cand = {}'.format(cand))
        loser = min(cand)
        print("removing {} as key from infl;decrementing friend\'s values \n".format(loser[2]))
        infl.pop(loser[2])
        cand.remove(loser)
        for val in graph[loser[2]]:
            if val in infl:
                infl[val]-=1
        if len(cand)==0:
            go=False
            return(set(infl.keys()))



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                'Could not find that file'))
   #graph = read_graph(open('graph2.txt','r'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
