#import numpy
import numpy as np
from Interfaces import Stack
from Interfaces import List

class ArrayStack(Stack, List):

    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemthods should be implemented. 
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple, 
        s = ArrayStack()
        print(s)
        print(len(s))
    '''
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int):
        return np.zeros(n, np.object_)
    
    def resize(self):
        '''
            Resize the array
        '''
        b = self.new_array(max(1,(self.n)*2))
        for i in range(self.n):
            b[i] = self.a[i] #copy the element from list_a to list_b

        self.a = b #set a equal to b to implement other function

    def get(self, i : int) -> object:
        if 0 < i or i >= self.n: #make sure the a[i] in the range
            return self.a[i]

    def set(self, i : int, x : object) -> object:
        if 0 < i or i >= self.n: # make sure the i inside the range of n
            y = self.a[i] #temp_value
            self.a[i] = x
            return y

    
    def add(self, i: int, x : object) :
        #print(i)
        if (0 > i) or (i > self.n): #check the i inside the n range
            raise IndexError()
        if len(self.a) == self.n:
            ArrayStack.resize(self)
        for j in range(self.n,i,-1):
            #if j > i: #shift all the j element to the right
            self.a[j] = self.a[j+1]
        #x  = self.a[i]
        self.a[i]=x #overwriting with a new value
        self.n = self.n +1 #incrementing number of element

        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
    def remove(self, i : int) -> object:
        if 0 > i or i >= self.n:#making sure the i inside the range
            raise IndexError()
        x = self.a[i]
        for j in range(i,self.n-2):
            self.a[j] = self.a[j+1] #move elements to the left
        self.n = self.n -1 #decrement the number of elements

        '''
            remove element i and shift all j > i one 
            position to the left
        '''
        if len(self.a) > (self.n)*3: #check if need the resize to reduce the capacity
            ArrayStack.resize(self)

        return x
    def push(self, x : object) :
        self.add(self.n, x)
    
    def pop(self) -> object :
        return self.remove(self.n-1)

    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n
        
    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x







