from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value


    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: object) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        bin = self._hash(key) #determind the bin of the list
        for i in range(self.t[bin].size()): #check each item to check if the key match
            if self.t[bin].get(i).key == key: #if yes, return the key
                return self.t[bin].get(i).value
        return None #otherwise, return None

    def add(self, key: object, value: object):
        if self.find(key) is not None: #check if the item already exsts or not
            return False #if yes, return False
        if self.n == len(self.t): #check the size
            #print('size:',(len(self.t)))
            self.resize()

        bin = self._hash(key)
        item = self.Node(key,value) #create a new node with key and value
        self.t[bin].add(0,item) #insert the new node as the head of the list
        self.n = self.n +1 #increase n elements
        return True

    def remove(self, key: int) -> object:
        bin = self._hash(key) #determind the bin where the node with given key should be store
        for i in range(self.t[bin].size()):#check for every node, whether the key item matches the given key
            if self.t[bin].get(i).key == key: #checking
                remove_val = self.t[bin].remove(i) #if yes, remove it
                self.n = self.n - 1 #decrement the n element
                if len(self.t) > 3*self.n: #check the size
                    self.resize()
                return remove_val #if found, remove the value and return the remove_val
        return None #return false if hte key doesn't found anywhere in the table




    def resize(self):
        if self.n == len(self.t): #if the numbe rof items in the table is the same as the number of bins, then create a new table
            self.d += 1
        else:
            self.d -=1
        temp = self.alloc_table(2**self.d) #if not, create a temp to store halp the number of bins
        for j in range(len(self.t)): #for every list in the table t, copy each item into the table temp
            for i in range(self.t[j].size()):
                bin = self._hash(self.t[j].get(i).key)
                temp[bin].add(0,self.t[j].get(i))
        self.t = temp #assign t as temp

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"

#
# c= ChainedHashTable()
# c.add(1,'First')
# c.add(2,'Second')
# c.add(3,'Third')
# c.add(4,'Fourth')
# c.add('a','letter a')
# print(c)
# print(c.find(4))
# print(c.find('First'))