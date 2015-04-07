from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):#7
    people=defaultdict(set)
    for line in file.readlines():
        line=line.strip().split(";")
        people[line[0]].add(line[1])
        people[line[1]].add(line[0])
    return dict(people)
    
def print_graph(graph):#4
    print("\nGraph: source nodes (ordered) -> destination nodes (ordered)")
    keys=list(graph.keys())
    keys.sort()
    for name in keys:
        values=list(graph.get(name))
        values.sort()
        print("   {} -> {}".format(name, ", ".join(values)))

def find_influencers(graph):#11
    infl,cand={}, []
    for key in graph.keys():
        infl[key]=len(graph.get(key))-ceil(len(graph.get(key))/2)
        if infl[key]>=0:
            cand.append((infl.get(key),len(graph.get(key)),key))
    positive_values_in_infl=True
    m=cand[0]
    while positive_values_in_infl==True:
        for item in cand:
            if item[0]<m[0]:
                m=item
            elif item[0]==m[0]:
                if item[1]<m[1]:
                    m=item
                elif item[1]==m[1]:
                    if item[2]<m[2]:
                        m=item
        node_to_remove=m[2]
        if m[2] in infl.keys():
            del infl[m[2]]
        count=1
        for value in infl.values():
            if value:
                count+=1
        if count==0:
            positive_values_in_infl=False
        for key in infl.keys():
            for value in graph.get(key):
                if value==node_to_remove:
                    infl[key]=infl.get(key)-1
    
    return set(infl.keys())                  


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
