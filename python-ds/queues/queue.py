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
        if not self.is_empty():
            return self.items.pop()


    def peek(self):
        if not self.is_empty():
            return self.items[-1].value


    def __len__(self):
        return self.size()


    def size(self):
        return len(self.items)