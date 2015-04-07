
# primes is used to test code you write below
from predicate import is_prime
def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1 
    
def increases(iterable,threshold):
    it = iter(iterable)
    try:
        answer = []
        new = next(it)
        i = 0
        while True:
            old,new,i = new,next(it),i+1
            if new >= old + threshold:
                answer.append(i)
    except StopIteration:
        return answer
 
 
class Permutation:
    def __init__(self,p):
        self.p = p
        
#    def _gen(p,start):
#        k = start
#        while True:
#            yield k
#            k = p[k]
#            if k == start:
#                raise StopIteration
#    def __iter__(self):
#        return Permutation._gen(self.p, min(self.p.keys()))
#
#    def iter_from(self,start):
#        assert start in self.p,'Permutation.iter_from: start('+str(start)+') not a key'
#        return Permutation._gen(self.p,start)
            
            
    class P_iter:
        def __init__(self,p,start):
            self.p     = p 
            self.start = start
            self.k     = start
            self.done= len(p) == 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.done:
                raise StopIteration
            answer = self.k
            self.k = self.p[self.k]
            self.done = self.k == self.start
            return answer 

    def __iter__(self):
        return Permutation.P_iter(self.p,min(self.p.keys()))       
         
    def iter_from(self,start):
        assert start in self.p,'Permutation.iter_from: start('+str(start)+') not a key'
        return Permutation.P_iter(self.p,start)
    
    
def compress(vit,bit):
    for v,b in zip(vit,bit):
        if b:
            yield v
            
            
def interleave(*args):
    iters = [iter(i) for i in args]
    while True:
        for i in iters:
            yield next(i)


if __name__ == '__main__':
    import driver
    from goody import irange
    import traceback
    
    driver.driver() # type quit in driver to return and execute code below
    
    # Test increases; add your own test cases
    print(increases([0,1,-1,3,7,4,5,3,2,4,8],2))
    print(increases(primes(1000),14))
    
    
    # Test Permutation; add your own test cases
    for i in Permutation({'a':'c', 'b':'a', 'c':'d', 'd':'b'}):
        print(i,end='')
    print()
    
    for i in Permutation({'a':'c', 'b':'a', 'c':'d', 'd':'b'}).iter_from('d'):
        print(i,end='')
    print()
    
    for i in Permutation({1:8, 8:4, 4:6, 6:2, 2:3, 3:7, 7:5, 5:1}):
        print(i,end='')
    print()
    
    for i in Permutation({1:8, 8:4, 4:6, 6:2, 2:3, 3:7, 7:5, 5:1}).iter_from(2):
        print(i,end='')
    print()
    
    try:
        for i in Permutation({'a':'c', 'b':'a', 'c':'d', 'd':'b'}).iter_from('x'):
            print(i,end='')
        print()
    except AssertionError:
        traceback.print_exc()

        
    # Test compress; add your own test cases
    for i in compress('abcdefghijklmnopqrstuvwxyz',
                      [is_prime(i) for i in irange(1,26)]):
        print(i,end='')
    print()
    
    
    # Test interleave; add your own test cases
    for i in interleave('abcde',[1,2,3,4,5],'vwxyz'):
        print(i,end='')
    
