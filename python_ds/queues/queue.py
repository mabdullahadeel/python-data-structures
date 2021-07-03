"""
    Que is another data structure that works on
    the principle of FIFO which means first in
    first out.
"""

class Queue(object):
    def __init__(self):
        self.items = []


    def enqueue(self, item):
        """ add new item to the queue """
        self.items.insert(0, item)


    def is_empty(self):
        """ remove the last item from the queue and return it """
        return len(self.items) == 0


    def dequeue(self):
        """ remove one item from the last and return it."""
        if not self.is_empty():
            return self.items.pop()


    def peek(self):
        """
            Returns the last element form the list
            which actually will be the front of the
            queue.
        """
        if not self.is_empty():
            return self.items[-1]


    def __len__(self):
        return self.size()


    def size(self):
        return len(self.items)