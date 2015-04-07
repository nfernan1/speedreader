from generator import transform, running_count, n_with_pad, sequence, alternate
#import flatten # uncomment this line if you wrote flatten

# lets is a generator that iterates through string
def lets(string):
    for i in range(len(string)):
        yield string[i]

        

for i in transform('abCdeFg',str.upper):
    print(i,end=' ')
print()

for i in transform(lets('abCdeFg'),str.upper):
    print(i,end=' ')
print()

  
   
for i in running_count('bananastand',lambda x : x in 'aeiou'): # is vowel
    print(i,end=' ')
print()

for i in running_count(lets('bananastand'),lambda x : x in 'aeiou'): # is vowel
    print(i,end=' ')
print()



for i in n_with_pad('abcdefg',3,None):
    print(i,end=' ')
print()

for i in n_with_pad('abcdefg',10,'?'):
    print(i,end=' ')
print()

for i in n_with_pad('abcdefg',10):
    print(i,end=' ')
print()

for i in n_with_pad(lets('abcdefg'),10):
    print(i,end=' ')
print()



for i in sequence('abcde','fg','hijk'):
    print(i,end=' ')
print()

for i in sequence(lets('abcde'),lets('fg'),lets('hijk')):
    print(i,end=' ')
print()



for i in alternate('abcde','fg','hijk'):
    print(i,end=' ')
print()

for i in alternate(lets('abcde'),lets('fg'),lets('hijk')):
    print(i,end=' ')
print()



# uncomment the following line if you wrote flatten
#for i in flatten([1,2,[3,4,(5,6,7,{'abc':1,'xyz':2}),8,9],10]): print(i,end=' ')