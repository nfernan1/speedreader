from linkedlist33 import *
from queue33 import *

x = LinkedList()

# 6 7 8 9 10 11


x.append(9)
x.prepend(8)
x.prepend(7)
x.append(10)
x.prepend(6)
x.append(11)

##x.remove_last()
print(x)
x.remove_first()
x.remove_last()
##
print(type(x[2:5]))

##print(x[1])
##print(x[4:5])
##print(x._slicelist(range(3,5)))
##x[2] = 5
##print()
##print(x[3:5])
##print(x[2:3], '34533453')


##print(x._head)
##print(x._head.next)
##print(x._head.next.next)
##print(x._tail)

print(x)            

        
