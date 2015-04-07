#Victor Hsiao
#82542906
#Lab 3


from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    friends=dict()
    for i in file.readlines():
        x,y=i.strip().split(sep=';')
        if x not in friends:
            friends[x]={y}
        else:
            friends[x].add(y)
        if y in friends:
            friends[y].add(x)
        else:
            friends[y]={x}
    return friends

def print_graph(graph):
    print("Graph: source nodes(ordered) -> destination nodes(ordered)")
    for k,v in sorted(graph.items()):
        values=""
        for m in sorted(v):
            values+=m+", "
        print("{} -> {}".format(k,values[:-2]))
        
def find_influencers(graph):
    def negative(dictionary):
        neg=0
        for i in dictionary.values():
            if i < 0:
                neg+=1
        return neg != len(dictionary)
    infl=dict()
    for i in graph:
        infl[i]=len(graph[i])-ceil((len(graph[i])/2))

    while negative(infl):
        cand=[]
        for i in infl:
            if infl[i]>=0:
                cand.append((infl[i],len(graph[i]),i))
        lowest=cand[0]
        for i in cand:

            if i[0]>lowest[0]:
                pass
            elif i[1]>lowest[1]:
                pass
            elif i[2]>lowest[2]:
                pass
            elif i[0]<lowest[0]:
                lowest=i
            elif i[1]<lowest[1]:
                lowest=i
            elif i[2]<lowest[2]:
                lowest=i

        for key in graph:
            if lowest[2] in graph[key]:
                if key in infl:
                    infl[key]-=1
        infl.pop(lowest[2])

    return {i for i in infl.keys()}
    




# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file',default='graph.txt'))    
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
