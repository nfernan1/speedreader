from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self,values=[]):
        self.counts = defaultdict(int)
        for v in values:
            self.counts[v] += 1
    
    def __str__(self):
        return 'Bag('+', '.join([str(k)+'['+str(v)+']' for k,v in self.counts.items()])+')'

    def add(self,v):
        self.counts[v] += 1
    
    def __iter__(self):
        def gen(x):
            for k,v in sorted(x.items(),key= lambda x : (-x[1],x[0])):
                for i in range(v):
                    yield k  
        return gen(dict(self.counts))
    
    
if __name__ == '__main__':
    #add any other debugging code you wish here
    
    b = Bag(['a','b','b','c','c','c','d','d','d','e','e','f'])
    print('For b =',b, 'iteration should print')
    print('correct = cccdddbbeeaf')
    print('answer  = ',end='')
    for i in b:
        b.add(i)
        print(i,end='')
    print()
    
    print('\nFor b=',b, 'iteration should print')
    print('correct = ccccccddddddbbbbeeeeaaff')
    print('answer  = ',end='')
    for i in b:
        print(i,end='')
    print()
