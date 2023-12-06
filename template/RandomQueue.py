import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self):
        if self.n <= 0:
            raise IndexError()

        r = random.randint(0,self.n - 1)
        v = self.a[(self.j + r)%len(self.a)]
        self.a[(self.j+r) % len(self.a)] = self.a[self.j]
        self.a[self.j] = v
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        #super.__init__()
        return super().remove()

