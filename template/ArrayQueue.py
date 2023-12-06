import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0 #size
        self.j = 0 #head
        self.a = self.new_array(1) #initial size = 1 for array

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, object)

    def resize(self):
        #print('resize')
        b = self.new_array(max(1,2*(self.n)))

        for k in range(self.n):
            b[k] = self.a[(self.j + k)%len(self.a)]

        self.a = b
        self.j = 0 #update the head equal to 0 in the new array
        '''
            Resize the array
        '''

    def add(self, x: object):
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if len(self.a) == self.n:
            self.resize()
        self.a[(self.j + self.n)%len(self.a)] = x
        #x = self.a[(self.j +self.n)%len(self.a)]
        self.n = self.n+1


    def remove(self):
        if self.n <= 0:
            raise IndexError()

        x = self.a[self.j]
        self.j = (self.j +1)% len(self.a)
        self.n = self.n - 1

        if len(self.a) >= 3*(self.n):
            self.resize()
            '''
            remove the first element in the queue
        '''
        return x

    def size(self):
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x




