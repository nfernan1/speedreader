#Nicholas Fernando 12659548
from linkedlist33 import *

class Queue:

    def __init__(self):
        'Creates  a doubly linked list to use for a queue'
        self._ll = LinkedList()

    def enqueue(self, item):
        'Appends an item to the linked list'
        return self._ll.append(item)

    def dequeue(self):
        'Removes the first element of the list then returns it'
        result = self.front()

        self._ll.remove_first()

        return result

    def front(self):
        'Returns the first element of the queue'
        if len(self._ll) == 0:
            raise IndexError('Empty Queue')

        return self._ll[0]

    def __len__(self):
        return len(self._ll)

    def __iter__(self):
        'Iterates the queue in first-to-last order'
        return iter(self._ll)


    def __repr__(self):
        'Creates a canonical representation of the queue'
        return '{}'.format(self._ll)

