from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    dictionary = defaultdict(set)
    infile = file.readlines()
    for line in infile:
        s = line.split(';')       
        dictionary[s[0]].add(s[1][0])
        dictionary[s[1][0]].add(s[0])
    return dictionary

def print_graph(graph):
    x= []
    items_list= []
    lst = []
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    
    for items in graph.items():
        x.append(items)
    x.sort()
    
    for items in x:
        items_list.append(items)
        items_list.sort()
        value_list = []
        for values in items[1]:
            value_list.append(values)
        value_list.sort()
        lst.append(value_list)
    
    for i in zip(items_list,lst):
        y=''
        for x in i[1]:
            y += str(x)+', '
        print('\t{} -> {}'.format(i[0][0],y[:-2]))
   
def find_influencers(graph):
    infl = dict()
    
    for items in graph.items():
        infl[items[0]]=ceil(len(items[1])-len(items[1])/2)
    



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
