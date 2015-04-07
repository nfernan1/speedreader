#Nicholas Fernando 12659548

from linkedlist33 import *
import unittest

class testlinkedlist(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

            
    def test_append(self):
        'Tests if the append method appends to the end of the list setting head and tail'
        
        self.ll.append(9)

        self.assertEqual(self.ll._head.data, 9)
        self.assertEqual(self.ll._tail.data, 9)

    def test_prepend(self):
        'Tests if the prepend method adds an item to the beginning of the list'
        
        self.ll.append(9)
        self.ll.append(10)

        headchange = self.ll.prepend(8)
        self.assertEqual(self.ll._head.data, 8)

    def test_remove_first(self):
        'Tests if the remove_first method removes an item at the beginning of the list'
        self.ll.append(1)
        self.ll.prepend(0)

        
        self.ll.remove_first()

        self.assertEqual(self.ll._head.data, 1)

    def test_remove_last(self):
        'Tests if the remove_last method removes an item at the end of the list'

        self.ll.append(1)
        self.ll.prepend(0)
        self.ll.append(2)

        self.ll.remove_last()

        self.assertEqual(self.ll._tail.data,1)


    def test_deleteitem(self):
        'Tests if a node can be deleted in the linked list'

        self.ll.append(1)
        self.ll.prepend(0)
        self.ll.append(2)

        del self.ll[1]

        check = []

        for i in self.ll:
            check.append(i)

        self.assertEqual(check, [0,2])

    def test_deleteslice(self):
        'Tests if you can delete slice'
        
        self.ll.append(1)
        self.ll.prepend(0)
        self.ll.append(2)    
        self.ll.append(3)
        self.ll.append(4)

        del self.ll[0:2]
        
        check1 = []
        for i in self.ll:
            check1.append(i)

        self.assertEqual(check1, [2,3,4])

        
    def test_setitemstonew(self):
        'changes variables in the linked list'

        self.ll.append(1)
        self.ll.prepend(0)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)

        self.ll[0] = 5

        check = []
        for i in self.ll:
            check.append(i)
            
        self.assertEqual(check, [5,1,2,3,4])

    def test_settingitemslice(self):
        'sets item slice'
        self.ll.append(1)
        self.ll.prepend(0)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)
        self.ll[0:3] = [5]

        check1 = []
        for i in self.ll:
            check1.append(i)

        self.assertEqual(check1, [5,5,5,3,4])

    def test_iterationofthelinkedlist(self):
        'checks to see if the linked list can be iterated through'
        self.ll.append(1)

        for i in self.ll:
            self.assertEqual(i,1)

    def test_gettinganitemindex(self):
        'Gets the node at the index'
        
        self.ll.append(1)
        self.ll.prepend(0)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)

        a = self.ll[2]

        self.assertEqual(a.data, 2)

    def test_gettingitemslice(self):
        'Gets the nodes from the slice index'

        self.ll.append(1)
        self.ll.prepend(0)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)

        b = self.ll[1:5]
        check = []
        for i in b:
            check.append(i.data)

        self.assertEqual(check, [1,2,3,4])

if __name__ == '__main__':
    unittest.main(exit = False)


