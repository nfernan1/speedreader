import math
from goody import type_as_str

class Point:
    
    def __init__(self,x,y):
        assert type(x) is int,'Point.__init__: x('+str(x)+') is not an int('+type_as_str(x)+')'
        assert type(y) is int,'Point.__init__: y('+str(y)+') is not an int('+type_as_str(y)+')'
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def __str__(self):
        return '(x='+str(self.x)+',y='+str(self.y)+')'
    
    def __bool__(self):
        return self.x != 0 or self.y != 0
        
    def __add__(self,right):
        if type(right) is Point:
            return Point(self.x+right.x,self.y+right.y)
        else:
            raise TypeError('Point.__add__: right('+str(right)+') not Point('+type_as_str(right)+')')

    def __mul__(self,right):
        if type(right) is int:
            return Point(self.x*right,self.y*right)
        else:
            raise TypeError('Point.__mul__: right('+str(right)+') not Point('+type_as_str(right)+')')

    def __rmul__(self,left):
        if type(left) is int:
            return Point(left*self.x,left*self.y)
        else:
            raise TypeError('Point.__rmul__: left('+str(left)+') not int('+type_as_str(left)+')')

    def __lt__(self,right):
        if type(right) is Point:
            return math.sqrt(self.x**2 + self.y**2) < math.sqrt(right.x**2+right.y**2)
        if type(right) is int or type(right) is float:
            return math.sqrt(self.x**2 + self.y**2) < right
        else:
            raise TypeError('Point.__lt__: right('+str(right)+') int or float('+type_as_str(right)+')')

    def __getitem__(self,index):
        if type(index) not in [int,str]:
            raise IndexError('Point.__getitem__: index('+str(index)+') must be str or int('+type_as_str(index)+')')
        if type(index) is str: 
            if index in ['x','y']: 
                return self.x if index=='x' else self.y
            else:
                raise IndexError('Point.__getitem__: index('+str(index)+') must be x or y)')
        if type(index) is int: 
            if 0<=index<=1 :
                return self.x if index==0 else self.y
            else:
                raise IndexError('Point.__getitem__: index('+str(index)+') must be 0 or 1')
        
    def __call__(self,x,y):
        assert type(x) is int,'Point.__call__: x('+str(x)+') is not an int('+type_as_str(x)+')'
        assert type(y) is int,'Point.__call__: y('+str(y)+') is not an int('+type_as_str(y)+')'
        self.x,self.y = x,y
        

from collections import defaultdict
class History:
    def __init__(self):
        self.history = defaultdict(list)
    
    def __getattr__(self,name):
        back = name.count('_prev')
        if back == 0 or not name.endswith('_prev') :
            raise NameError('History.__getattr__: name('+name+') has no _prev')
        real_name = name[:-5*back]
        if real_name not in self.history:
            raise NameError('History.__getattr__: name('+real_name+') is not an attribute of the object')
        old = self.history[real_name]
        if back < len(old):
            return old[-back-1]
        else:
            return None
       
    def __setattr__(self,name,value):
        if name.find('_rev') != -1:
            raise NameError('History.__setattr__: name('+name+') cannot contain _prev')
        if 'history' in self.__dict__:
            self.history[name].append(value)
        self.__dict__[name] = value
     
    def __getitem__(self,index):
        if index > 0:
            raise IndexError('History.__getitem__: index('+str(index)+') > 0')
        return {k:v[index-1] if abs(index) < len(v) else None for k,v in self.history.items()}
     



if __name__ == '__main__':
    import driver
    driver.driver()
