class DictStr_SetInt:
    def __init__(self,adict):
        self._data = adict
    
    def __str__(self):
        return str(self._data)
        
    def __iter__(self):
        def gen(d):
            for k in d.keys():
                for v in d[k]:
                    yield (k,v)
        return gen(dict(self._data))
      

if __name__ == '__main__':
    #add any other debugging code you wish here
    
    d = DictStr_SetInt(dict(abcde={1,2},lmnop={2},uvxyz={1,2,3}))
    print('For d =',d._data, 'iteration should print')
    print("correct = ('lmnop', 2)('abcde', 1)('abcde', 2)('uvxyz', 1)('uvxyz', 2)('uvxyz', 3) or any other order")
    print('answer  = ',end='')
    for i in d:
        print(i,end='')
    print()
