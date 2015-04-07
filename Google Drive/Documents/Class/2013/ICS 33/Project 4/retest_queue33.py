#Nicholas Fernando 12659548

from queue33 import *
import unittest

class testlinkedlist(unittest.TestCase):

    def setUp(self):
        self._queue = Queue()

    def test_after_enqueuing_one_element_it_is_at_front(self):
        self._queue.enqueue('dude')
        self.assertEqual(self._queue.front(), 'dude')


if __name__ == '__main__':
    unittest.main(exit = False)
