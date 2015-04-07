from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        tokens = line.strip().split(';');
        graph[tokens[0]].add(tokens[1]) #Token 0 -> set with token 1
        graph[tokens[1]].add(tokens[0]) #Token 1 -> set with token 0
    #rof
    return dict(graph)

def print_graph(graph):
    #Format and Sort
    ordered_graph = sorted(list(graph.items()))
        
    #Print
    print('\nGraph: source nodes (ordered) -> destination nodes (ordered)')
    for i in ordered_graph:
        connected_str = ''
        for j in sorted(list(i[1])): #Print sorted 
            connected_str = connected_str + '{}, '.format(j) #Build connected nodes string.
        print('  {} -> {}'.format(i[0], connected_str[:-2]))
    print()

def find_influencers(graph):
    #Influences
    infl = defaultdict(int) #default int is 0
    for i in graph.keys():
        f = friends(graph,i)
        infl[i] = f - ceil(f/2)
        
    #Candidates
    cand = sorted([(i[1],friends(graph,i[0]),i[0]) for i in infl.items()])
    while(len(cand) > 0): #Cycle through candidate list until it is empty.
        mini = cand.pop(0) #Pop minimum
        infl.pop(mini[2]) #Remove associated key from influence dictionary.
        for i in infl.keys():
            if mini[2] in graph[i]: #Modify friends.
                infl[i] -= 1
                if infl[i] < 0: #If negative, remove from candidate list.
                    exclude(cand, i)
                    
    return set(infl.keys())
                    

''' Helper Functions '''    
def friends(graph, key):
    return len(graph[key])

def exclude(cand, key):
    for i in cand:
        if key == i[2]:
            cand.remove(i)


# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
