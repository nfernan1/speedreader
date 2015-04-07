from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    resultDict = {}
    with open(file, 'r') as inputFile:
        data = inputFile.read().splitlines()
        for i in data:
            i = i.split(';')
            key = i[0]
            value = i[1]
            for k, v in zip(key, value):
                if k in resultDict:
                    try:
                        resultDict[k].add(v)
                        resultDict[v].add(k)
                    except KeyError:
                        resultDict[v] = set(k)
                else:
                    resultDict[k] = set(v)
                    resultDict[v] = set(k)
                

    return resultDict
                    
            

def print_graph(graph):
    
    keyList = []
    valueList = []
    for i in graph.keys():
        keyList.append(i)
        valueList.append(graph[i])
    
    keyList.sort()
    valueList.sort()
    print(valueList)

    for key in keyList:
        print('{} -> {}'.format(key, graph[key]))
    
  
           
def find_influencers(graph):
    infl = {}
    cand = []
    for key in graph:
        count = len(graph[key])
        calc = count - (ceil(count / 2)) 
        infl[key] = calc
        
        cand.append((infl[key], count, key))
            
    cand.sort(key = lambda x: x[0])
    
    min = cand[0]
    toDelete = min[2]
    print(infl)            
    
    for friend in graph.keys():
        if toDelete in graph[friend]:
            print(friend)
            infl[friend] - 1
                
    del infl[toDelete]
    del cand[0]          
                      
    return infl
    


#Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
