#Nicholas Fernando 12659548

class LinkedList:
    'Creates a linked list'

    def __init__(self):
        self._head = None
        self._tail = None
        
        self._size = 0

    def __len__(self):
        return self._size


    class _Node:
        'Makes a node inside the linked list'

        def __init__(self, data=None, n=None, p=None):
            self.data = data
            self.next = n
            self.prev = p
            self._move = (self.prev, self.next)

        def setdata(self, newdata):
            self.data = newdata

        def get(self, move):
            return self._move[int(move)]

        def __repr__(self):
            return '{}'.format(self.data)
        
    def append(self, item):
        'Adds an element to the end of the list'
        new_node = self._Node(item, None,self._tail)
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
        new_node = self._Node(item,self._head, None)
        new_node.data = item
        
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
            
        self._size += 1
        
    def remove_first(self):
        'Removes the last element of the list'
        if self._size > 0:
            self._head = self._head.next
            self._tail = self._tail.prev
            
        else:
            self._tail = self._tail.prev
            self._tail.next = None
                
        if self._size < 0:
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
    
        if self._size == 0:
            raise IndexError('Can\'t delete in empty list.')
        if type(index) == int:
            if index == curnode.data:
                if curnode.next == None:
                    self.remove_first()
                    return
                
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
                
            for idx in self._slicelist(index):
                del self[idx]

                        

            self._size -=1             


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
        

    def _slicelist(self,index):
        'Returns a list of slice indexes'
        slicelist = []

        step = self._startstopstep(index.step,1,1,1)
        start = self._startstopstep(index.start,step,0,self._size-1)
        stop = self._startstopstep(index.stop,step,self._size,-1)

        for i in range(start,stop,step):
            slicelist.append(i)

        return slicelist
    
    
    
    def __getitem__(self, index):
        'The linked list can be indexed and sliced'
        counter = 0
        node = self._head
        
        if type(index)==int:
            ni = self._normalize_int_index(index)
            while counter != ni:
                counter += 1
                node = node.next
            return node
        
        if type(index) == slice:
            
            noix = self._slicelist(index)
            results = []
            
            for idx in noix:
                results.append(self[idx])
                
            return results

        
    def __setitem__(self, index, newdata):
        'Places an object at the specified index'
        node = self._head

        if type(index) == int:
            if self._size >= index >= 0:
                for i in range(index):
                    node = node.next

                return node.setdata(newdata)
            
            elif index < 0: 
                index += self._size
                
            else:
                raise IndexError('Index out of range.')
            
        if type(index) == slice:
            try:
                value = None
                for i in newdata:
                    value = i
                    
                for i in self._slicelist(index):
                    self[i] = value
            except TypeError:
                raise TypeError('Can only assign an iterable')

                
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

