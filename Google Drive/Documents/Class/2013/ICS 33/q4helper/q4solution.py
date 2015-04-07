
# primes is used to test code you write below
from predicate import is_prime
import types
def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1 
    
def increases(iterable,threshold):
    
    lst= []
    while True:
        if type(iterable) is types.GeneratorType:
            next1 = next(iterable)
            next2 = next(iterable)
            for idx, element in enumerate(iterable):
                    next1 = next2
                    next2 = element 
                    
                    if next2 >= next1+threshold:
                        lst.append(idx+2)
                
        else:
            for idx, element in enumerate(iterable):
                current = element
                new_elem = iterable[(idx + 1) % len(iterable)]
                     
                if new_elem >= current+threshold:
                    lst.append(idx+1)
                 
        return lst


class Permutation:
    
    def __init__(self, closed_dict):
        self._closed_dict = closed_dict
    
    class P_iter:
        
        def __init__(self, closed_dict):
            self._dict = closed_dict
            


            
        def __next__(self): 
            
            toIter = iter(sorted(self._dict))
            
            yield next(toIter)
            
            
        
        def __iter__(self): 
            return self
        
    def iter_from(self, start_key): 
        if start_key not in self._closed_dict:
            raise AssertionError
        
        
        return self.P_iter(start_key)
        
    
    def __iter__(self): 
        for i in self._closed_dict:
            yield self._closed_dict[i]
        
#         return self.P_iter(self._closed_dict) 
    


for i in Permutation({'a':'c', 'b':'a', 'c':'d', 'd':'b'}):
    print(i,end='')
print()

#===============================================================================
# for i in Permutation({'a':'c', 'b':'a', 'c':'d', 'd':'b'}).iter_from('d'):
#     print(i,end='')
# print()
#===============================================================================
        
def compress(vit,bit):
    for elem1, elem2 in zip(vit,bit):
        if elem2 == True:
            yield elem1    
    
    
def interleave(*args):
    lst = [iter(value) for value in args]

    while True:
        for element in lst:
           yield next(element)
        


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
    
