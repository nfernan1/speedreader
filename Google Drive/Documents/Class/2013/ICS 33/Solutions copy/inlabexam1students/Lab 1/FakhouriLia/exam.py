from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    result = dict()
    for lines in file.readlines():
        line = lines.strip().split(';')

        for key in line[0]:
            result[key]= {line[1]}
            result[line[1]] = {key}
            if line[1] in result.keys():
                result[line[1]].add(key)
            
    return result
        

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for key, value in sorted(graph):
        print('  {} -> {}'.format(key,sorted(value)))
    
    
    
def find_influencers(graph):
    infl = dict()
    cand = []
    popped = ()
    #Influence
    nodes = list(graph.keys())
    for node in nodes:
        num_friends = len(graph.get(node))
        value_node = num_friends - ceil(len(graph.get(node))/2)
        
        infl[node] = value_node
        
        #Candidates
        for key in infl.keys():
            if key > 0:
                cand.append((value_node, num_friends, node))
        
        
        #Minimum and Remove
        check_list = []
        for c in cand:
            check_list.append(min(c[0]))
            if len(check_list)== 1:
                popped.add(c)
                cand.pop(c)
            else:
                check_list.clear()
                check_list.append(min(c[1]))
                if len(check_list) == 1:
                    popped.add(c)
                    cand.pop(c)
                else:
                    check_list.clear()
                    check_list.append(min(c[2]))
                    popped.add(c)
                    cand.pop(c)
        
        #Decrement values
        value_friends = graph.get(popped)
        for person in value_friends:
            for c in cand:
                if person in c[2]:
                    c[1] -= 1
                    
    return infl

# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
