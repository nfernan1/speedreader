#Chenguang Li Lab1
from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
#    file = goody.safe_open("Please enter the file",'r','Fail to open', default = '')
#    file = open("graph.txt","r") 
    l = []
    for i in file:
        l.append(i.rstrip().split(";"))
#        print(l)
    dic = dict()
    for line in l:
        dic.setdefault(line[0],set()).add(line[1])
#    print(dic)
#    return read_graph()
def print_graph(graph):
    print("source nodes (ordered) -> destination bides (ordered)")
    pointl = list(graph.keys)
    pointl.sort()
    for k in pointl:
        print("  " + k + " -> " + graph[k])
 
def find_influencers(dict1,str1):
    sing = [str1]
    cand = [str1]
    counter = 0
    for z in cand:
        for x in dict1(z):
            for y in  x:
                if y not in cand:
                    cand.append(y)
                for item in sing:
                    counter+=1
                if counter>= math.ceil(len(dict[y].keys().length()/2)):
                    sing.append(y)
                    counter =0                  
#def find_influencers(graph):
    
                        



# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                'Could not find that file'))
    print_graph(graph)
#    core = find_influencers(graph)
  #  print('Influencers =', find_influencers(graph))