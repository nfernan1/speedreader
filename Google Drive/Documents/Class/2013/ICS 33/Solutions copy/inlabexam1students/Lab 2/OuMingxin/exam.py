##Mingxin Ou Lab2

from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    answer = defaultdict(set)
    for line in file:
        data = line.strip().split(';')
        key = data[0]
        value = data[1]
        answer[key].add(value)
        answer[value].add(key)
    return dict(answer)
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for k in sorted(graph.keys()):
        values = list(graph[k])
        a_str = ''
        for i in sorted(values):
            a_str+=i
        print(k,'->',','.join(a_str))

def find_influencers(graph):
    pre_infl = defaultdict(int)
    for k,v in graph.items():
        pre_infl[k] = len(v) - ceil(len(v)/2)
    infl = dict(pre_infl)

#     for k,v in dict(infl).items():
#         cand.append((v,len(graph[k]),k))
    while True:
        cand = []
        for k,v in infl.items():
            if v>=0:
                cand.append((v,len(graph[k]),k))
        if cand == []:
            break
        removed_f = sorted(cand).pop(0)[2]
        to_decrement = graph[removed_f]
        infl.pop(removed_f)
        for dec in to_decrement:
            try:           
                infl[dec]= infl[dec]-1
            except:
                pass
    answer = {i for i in infl.keys()}
    return answer
        
    
            
        
        
    


d = read_graph(open('graph.txt'))
print_graph(d)
#find_influencers(d)
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
