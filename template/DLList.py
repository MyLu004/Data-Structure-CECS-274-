from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i >= self.n:
            return self.dummy
        if i < (self.n / 2):
            p = self.dummy.next #temp variable
            for k in range(i):
                p = p.next
        else:
            p = self.dummy.prev
            for k in range(self.n - i -1):
                p = p.prev
        return p

    def get(self, i) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.get_node(i).x


    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        if w is None:
            raise IndexError()
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n = self.n + 1
        return u

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError()
        return self.add_before(self.get_node(i), x)


    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n = self.n - 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        list = ''
        for i in range(self.n):
            list += self.get(i)
        if list[::-1] == list:
            return True
        return False

    def reverse(self):
        begin = self.dummy.next
        last = self.dummy.prev
        for i in range(int(self.n/2)):
            temp = begin.x #temp value
            begin.x = last.x #switch the position
            last.x = temp #then assign the last one with the temp value

            #up-date the value to be the next one
            begin = begin.next
            last = last.prev


    def swap(self):
        head_value = self.get_node(0).x

        tail_value = self.get_node(self.n-1).x

        head = self.set(0,tail_value)
        tail = self.set(self.n-1,head_value)





    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
'''
d = DLList()
d.add(0,'r')
d.add(1,'e')
d.add(2,'p')
d.add(3,'a')
d.add(4,'p')
d.add(5,'e')
d.add(6,'r')
# '''
# d = DLList()
# d.add(0,'A')
# d.add(1,'B')
# d.add(2,'C')
# d.add(3,'D')
# d.add(4,'E')
# d.add(5,'F')
# print(d)
# d.swap()
# print(d)
#
# d = DLList()
# d.add(0,'A')
# d.add(1,'B')
# d.add(2,'A')
# print(d.isPalindrome())