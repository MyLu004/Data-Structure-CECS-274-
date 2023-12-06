from Interfaces import Queue
import numpy as np


class SLLQueue(Queue):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def add(self, x: object):
        u = self.Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u

        self.tail = u
        self.n = self.n + 1

        return True


    def remove(self) -> object:
        if self.n == 0:
            raise IndexError()
        x = self.head.x #temp variable storing the value of head, which we are about to remove
        self.head = self.head.next #assign the head to the next_head_value
        self.n = self.n -1 #decrement the number of elements

        if self.n == 0:
            self.tail = None
        return x

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x


