from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file_name):
    mydict=defaultdict(set)
    with open(file_name,'r') as file:
        f=file.readlines()
        for line in f:
            new_line=line.strip().split(';')
            mydict[new_line[0]].add(new_line[1])
            mydict[new_line[1]].add(new_line[0])
        return dict(mydict)
            
        

def print_graph(graph):
    print('Graph: source nodes (ordered)','->','destination nodes (ordered)')
    for i,v in sorted(graph.items()):
        print(i,'->',v)
       

def find_influencers(graph):
    infl={}
    cand=[]
    for i,v in graph.items():
        infl.update({i:len(v)-(ceil(len(v)*0.5))})
        if not infl[i]<0:
            cand.append((infl[i],len(v),i))
    
            
    while len(infl)!=0:
        cand_check1=cand[0]
        cand_check2=cand[1]
        cand_check3=cand[2]
        
        #if min(cand[0])==1:
            #print('okay')
        #elif len(min(cand[0]))>1:
            #print('okay')
            #if 
        
        

 
    



# Script

if __name__ == '__main__':
    graph=read_graph('graph.txt')
    #graph = read_graph(safe_open('Enter name of file with graph', 'r',
                         #'Could not find that file'))
    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
