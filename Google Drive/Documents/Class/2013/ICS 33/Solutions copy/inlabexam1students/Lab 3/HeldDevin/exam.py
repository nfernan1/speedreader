from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)    
    for line in file.readlines():
        x = line.split(';')
        graph[x[0]].add(x[1].strip())
        graph[x[1].strip()].add(x[0])
    return graph

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for key, value in sorted(graph.items()):
        print(key, '->', ', '.join(sorted(value)))

def find_influencers(graph):
    infl = {}
    for key in graph.keys():
        infl[key] = len(graph[key]) - ceil(len(graph[key])/2)       
    candidates = [(infl[key], len(graph[key]), key) for key in infl.keys() if infl[key] >= 0]
    while len(candidates) >=2:
        inflval = [i[0] for i in candidates]
        to_go_through = []
        num = part = strr = go = ok = 0
        
        for tup in candidates:
            if tup[0] == min(inflval):
                num +=1
                to_go_through.append(tup)

        if num == 1:
            ok = 1
            toremove = candidates.pop(part-1)
            print('toremove',toremove)
        else:
            inflval2 = [i[1] for i in to_go_through]
            num = 0
            for tup in to_go_through:
                num+=1
                if tup[1] == min(inflval2) and tup[0] == min(inflval):
                    num +=1
                else:
                    to_go_through.pop(num-1)
            if num == 1:
                try:
                    toremove = to_go_through.pop(num-1)
                    print('toremove', toremove)
                except:
                    pass
            else:
                inflval3 = [i[2] for i in to_go_through]
                for tup in to_go_through:
                    strr+=1
                    if tup[2] == min(inflval3) and tup[1] == min(inflval2) and tup[0] == min(inflval):
                        print('this remove', tup, to_go_through[strr-1])
                        toremove = to_go_through.pop(strr-1)
                        break
        for item in candidates:
            go +=1
            if item[2] == toremove[2]:
                if ok != 1:
                    candidates.pop(go-1)
            elif toremove[2] in graph[item]:
                candidates.pop(go-1)
                
        print('remaining canddidates', candidates)
    return {x[2] for x in candidates}
            
            
                    
                #popped = inflval3.pop()

            
            
        
        

  
    #for key in infl.keys():
     #   if infl[key] >= 0:
      #      candidates.append((infl[key], len(graph[key]), key))
    #print(candidates)



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
