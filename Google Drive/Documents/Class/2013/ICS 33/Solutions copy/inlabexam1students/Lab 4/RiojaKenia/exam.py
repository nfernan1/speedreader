###Kenia D. Rioja-Naranjo
###48789974
###Lab4 ; In-Lab Exam I (22 October 2013)

from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    #f = safe_open('Enter name of file with graph', 'File not found', default='r')
    f_lines = file.readlines()#list of lines

    node_results = dict()
    littlef = []
    for f in f_lines:
        littlef.append(f.split(';'))
#------------------------------------------------
    for lf in littlef:
        if lf[0] not in node_results.keys():
            node_results[lf[0]] = {lf[1][0]}
            
            #---------------------------------------
            if lf[1][0] in node_results.keys():
                current_s = node_results[lf[1][0]]
                temp = []
                for s in current_s:
                    temp.append(s)
                temp.append(lf[0])
                node_results[lf[1][0]] = set(temp)
            
            else:
                node_results[lf[1][0]] = {lf[0]}
            
            #---------------------------------------
        
        else:
            current_s = node_results[lf[0]]
            temp = []
            for s in current_s:
                temp.append(s)
            temp.append(lf[1][0])
            node_results[lf[0]] = set(temp)
            
            if lf[1][0] in node_results.keys():
                current_s = node_results[lf[1][0]]
                temp = []
                for s in current_s:
                    temp.append(s)
                temp.append(lf[0])
                node_results[lf[1][0]] = set(temp)
                
            else:
                node_results[lf[1][0]] = {lf[0]}

#-------------------------------------------------        

    return node_results
    
#-------------------------------------------------------------------------------------------------------------------

def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    #Hint: use the join function defined in Python's str class
    for i in graph.keys():
        print('{} -> {}'.format(i, graph[i]))
    
 
def find_influencers(graph):
    result = set() #contains the influencer nodes, the people who will influence their friends
    for friend in graph.keys():
        friends = graph[friend]
        num_of_influenced = math.ceil(len(s))
    return result #should return {g,d}



# Script----------------------------------------------------------
if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
