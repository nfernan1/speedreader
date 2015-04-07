from queue33 import *
import unittest

class testqueue(unittest.TestCase):
    'Tests the Queue class'
    
    def setUp(self):
        self.q = Queue()
        self.q.enqueue(8)
        self.q.enqueue(9)
        self.q.enqueue(10)

        #Used to test the enqueue method
        self.test = Queue()

     
    def test_enqueueshouldappenditemtoendofqueue(self):
        'Tests the append method of the queue'
        indexlist = []
        
        self.test.enqueue(8) #first element
        self.test.enqueue(9) #second element
        self.test.enqueue(10) #third element

        for ele in self.test:
            indexlist.append(ele)
            
        self.assertEqual(indexlist[0], 8)
        self.assertEqual(indexlist[1], 9)
        self.assertEqual(indexlist[2], 10)
        

    def test_dequequeitemremovethefirstelementandreturnit(self):
        'Removes the first element then returns it'
        indexlist = []
        
        #Using dequeue() twice should leave the length of the list as 1 
        self.q.dequeue()
        self.q.dequeue()

        
        for ele in self.q:
            indexlist.append(ele)

        self.assertEqual(len(indexlist),1)


    def test_frontshouldreturnthefirstelementofthelist(self):
        'Removes the first element and return it'

        self.assertEqual(self.q.front().data, 8)


    def test_queueiterationmethod(self):
        'Tests the iteration ability of the queue'
        indexlist = []

        #Adds the elements of the queue into the indexlist
        #Indexlist should therefore consist of 8,9,10 in that order
        
        for ele in self.q:
            indexlist.append(ele)

        self.assertEqual(indexlist, [8,9,10])
            
            
          
if __name__ == '__main__':
    unittest.main(exit=False)
