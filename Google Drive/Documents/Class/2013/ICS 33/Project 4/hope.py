#Nicholas Fernando 12659548
class Node:
    'Makes a node inside the linked list'

    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    def __repr__(self):
        return '{}'.format(self.data)
    
class LinkedList:
    'Creates a linked list'

    def __init__(self):
        
        self._head = None
        self._tail = None
        
        self._size = 0

    def __len__(self):
        return self._size
        
    def append(self, item):
        'Adds an element to the end of the list'
        new_node = Node()
        new_node.data = item
        
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = self._tail.next

        self._size += 1


    def prepend(self, item):
        'Adds an element to the front of the list'
        new = Node()
        new.data = item
        
        if not self._head:
            self._head = new
            self._tail = new
        else:
            new.next = self._head
            self._head.prev = new
            self._head = new
            
        self._size +=1

    def remove_first(self):
        'Removes the first element of the list'

        if self._size > 0:
            self._head = self._head.next
            self._head.prev = None
            self._size -= 1
            
        else:
            raise IndexError('Cannot pop from empty List.')
        
        
    def remove_last(self): 
        'Removes the last element of the list'
        if self._size > 0:
            self._head = self._head.prev
            self._tail = self._tail.prev
            
        else:
            self._tail = self._tail.prev
            self._tail.next = None
                
        if self._size < 0:
            raise IndexError('Cannot pop from empty List.')
    
        
    def __delitem__(self, index):
        curnode = self._head
        deleted = False
        nod = []
        if self._size == 0:
            raise IndexError('Can\'t delete in empty list.')

        if index == curnode.data:
            print(1)
            if curnode.next == None:
                self.remove_first()
                return
                print(2)
            curnode = curnode.next
            self._head = curnode
            return
        
        while True:
            if curnode == None:
                deleted = False
                break
            
            nextnode = curnode.next
            if nextnode != None:

                if self[index] == nextnode:


                    nextnextnode = nextnode.next
                    curnode.next = nextnextnode

                    nextnode = None
                    deleted = True
                    break
                
            curnode = curnode.next
                
        if type(index) == slice:
                
            step = self._startstopstep(index.step,1,1,1)
            start = self._startstopstep(index.start, step, 0, self._size-1)
            stop = self._startstopstep(index.stop,step,self._size,-1)      
                
            for idx in range(start,stop,step):
                nod.append(self[idx])

            for i in nod:
                print(i)
                if i in self:
                    print(1)
                        

            self._size -=1             

#n.prev.next = n.next
#n.next.prev = n.prev
##################################################################

    def _normalize_int_index(self, index, is_allowed=False):
        if index < 0:
            index = self._size + index
        self._require_valid_nonnegative_index(index, is_allowed)
        return index

    def _require_valid_nonnegative_index(self, index, is_allowed):
        if not self._is_valid_nonnegative_index(index, is_allowed):
            raise IndexError('index out of bounds')

    def _is_valid_nonnegative_index(self, index, is_allowed):
        if is_allowed:
            return index >= 0 and index < self._size
        else:
            return index < self._size
    
    
    def _startstopstep(self, index, neg, pos, step):
        'Determines step and if the values are negative or positive'

        if index == None:
            if step > 0:
                return pos
            else:
                return neg
        else:
            return index


    def _slicelist(self, index):
        'Determines step and if the values are negative or positive'


        step = self._startstopstep(index.step,1,1,1)
        start = self._startstopstep(index.start, step, 0, self._size-1)
        stop = self._startstopstep(index.stop,step,self._size,-1)

        return range(start,stop,step)
    
        
    def __getitem__(self, index):
        'The linked list can be indexed and sliced'

        ni = self._normalize_int_index(index)
        counter = 0
        node = self._head

        if type(index) == int:
            while counter != ni:
                print(node)
                counter += 1
                node = node.next
       
        elif type(index) == slice:
            
            noix = self._slicelist(index)
            results = []
            
            for idx in noix:
                results.append(self[idx])
                
            return results
        
        

        if type(index) == slice:
          
            new_ll = LinkedList()

            step = self._startstopstep(index.step,1,1,1)
            start = self._startstopstep(index.start, step, 0, self._size-1)
            stop = self._startstopstep(index.stop,step,self._size,-1)

        
            for item in range(start,stop,step):
                new_ll.append(self[item])

            return new_ll
    

        
    def __setitem__(self, index, newdata):
        'Places an object at the specified index'
        node = self._head

        if type(index) == int:
            if self._size >= index >= 0:
                for i in range(index):
                    node = node.next

                return node.setdata(newdata)
            
            elif index < 0: ### negative 
                index += self._size
                
            else:
                raise IndexError('Index out of range.')
            
        if type(index) == slice:

            
            step = self._startstopstep(index.step,1,1,1)
            start = self._startstopstep(index.start, step, 0, self._size-1)
            stop = self._startstopstep(index.stop,step,self._size,-1)
            
            for i in range(start,stop,step):
                self[i] = newdata
            
##                while i == 0: //having a start and stop of 0 
##                    node = node.next
##                    
##                    self[] = newdata
##                    counter +=1
##                    if self._size == counter:
##                        break


    def __iter__(self):
        node = self._head
        while node is not None:
            
            yield node.data
            node = node.next


    def __repr__(self):
        ll_list = []

        for node in self:
            ll_list.append(node)
        return '{}'.format(ll_list)

