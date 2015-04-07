#Nicholas Fernando 12659548

from linkedlist33 import *
import unittest

class testlinkedlist(unittest.TestCase):

    def test_slices_return_linked_lists(self):
        items = ['another', 'sentence', 'for', 'testing', 'is', 'here']
        self._append_many(items)
        self.assertEqual(type(self._list[1:4]), LinkedList)

    def test_slice_indexing_with_positive_step(self):
        items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
        link = self._append_many(items)
        ll_list = []
        
        for i in link:
            ll_list.append(i)
            
        slice_list = ll_list[2:9:3]
        self.assertEquals(slice_list, ['c', 'f', 'i'])

    def test_slice_deletion_with_step(self):
        items = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']
        link = self._append_many(items)
        ll_list = []
        
        for i in link:
            ll_list.append(i)
            
        del ll_list[4:10:2]
        
        self.assertEquals(ll_list, ['z', 'y', 'x', 'w', 'u', 's', 'q', 'p', 'o', 'n'])


    def test_slice_assignment_with_step(self):
        items = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']
        link = self._append_many(items)
        
        ll_list = []
        
        for i in link:
            ll_list.append(i)
            
        ll_list[4:10:2] = ['a', 'b', 'c']
        
        self.assertEquals(ll_list, ['z', 'y', 'x', 'w', 'a', 'u', 'b', 's', 'c', 'q', 'p', 'o', 'n'])


    def _append_many(self,items):
        'Appends many items to linkedlist'
        self.ll = LinkedList()
        for i in items:
            self.ll.append(i)
        return self.ll

    def _prepend_many(self,items):
        'Prepends many items to linkedlist'
        self.ll = LinkedList()

        for i in items:
            self.ll.prepend(i)
        return self.ll
if __name__ == '__main__':
    unittest.main(exit = False)
