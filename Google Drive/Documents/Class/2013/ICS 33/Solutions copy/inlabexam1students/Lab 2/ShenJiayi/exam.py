from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    result=dict()
    for line in file:
        a,b=line.strip().split(';')
        if a not in result:
            result[a]=[b]
        else:
            result[a].append(b)
        if b not in result:
            result[b]=[a]
        else:
            result[b].append(a)
    for each in result.keys():
        result[each]=set(result[each])
    return result
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered) ')
    for each in sorted(graph.keys()):
        result=''
        for each in sorted(graph[each]):
            result+=each+', '
        print('{} -> {}'.format(each, result.strip(', ')))
        

def find_influencers(graph):
    print(graph)
    cand=[]
    infl=dict()
    for each in graph.keys():
        a=ceil(len(graph[each])-ceil(len(graph[each])/2))
        cand.append([a,len(graph[each]),each])
        infl[each]=a
    cand.sort()
    print(cand)
    print(infl)
    while len(cand)>1: 

        for each in graph.keys(): 
            if cand[0][2] in graph[each]:
                if each in infl.keys():
                    infl[each]-=1
                for member in cand:
                    if member[2]==each:
                        member=(infl[each],member[1],each)
        infl.pop(cand[0][2])
        for a in cand:
            if a[0]<0:
                cand.remove(a)
        cand=cand[1:]
        print(infl)
        print(cand)

        
        
graph = read_graph(open('graph.txt'))  
find_influencers(graph)     


# Script


if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
