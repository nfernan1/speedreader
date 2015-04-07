class Measurement:
    
    def __init__(self,bound1,bound2=None):
        if bound2 == None:
            bound2 = bound1
        if type(bound1) not in [int,float]:
            raise TypeError('Measurement.__init__: bound1('+str(bound1)+') not int/float')
        if type(bound2) not in [int,float]:
            raise TypeError('Measurement.__init__: bound2('+str(bound2)+') not int/float')
        if bound1 > bound2:
            bound1,bound2 = bound2,bound1
        self.low, self.high = bound1,bound2
    
    def __repr__(self):
        return 'Measurement('+str(self.low)+','+str(self.high)+')'

    def __str__(self):
        return str((self.low+self.high)/2)+'+/-'+str((self.high-self.low)/2)
     
    @staticmethod                                  
    def alt(value,error=0):
        return Measurement(value-error,value+error)
    
    def __add__(self,right):
        if type(right) not in [Measurement,int,float]:
            raise TypeError('Measurement.__add__: right('+str(right)+') not Measurement/int/float')
        if type(right) in [int,float]:
            right = Measurement(right)
        return Measurement(self.low+right.low,self.high+right.high)
    
    def __radd__(self,left):
        return self + left
    
    def __mul__(self,right):
        if type(right) not in [Measurement,int,float]:
            raise TypeError('Measurement.__mult__: right('+str(right)+') not Measurement/int/float')
        if type(right) in [int,float]:
            right = Measurement(right)
        all_mult = [self.low*right.low, self.low*right.high, self.high*right.low, self.high*right.high]
        return Measurement(min(all_mult),max(all_mult))

    def __rmul__(self,left):
        return self * left
    
    def __lt__(self,right):
        if type(right) not in [Measurement,int,float]:
            raise TypeError('Measurement.__lt__: right('+str(right)+') not Measurement/int/float')
        if type(right) in [int,float]:
            right = Measurement(right,right)
        return self.high < right.low
    
    def __gt__(self,right):
        return right < self
    
    def __eq__(self,right):
        return not (self<right or self>right)
    

    
    
if __name__ == '__main__':
    import driver
    driver.driver()        