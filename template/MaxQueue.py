from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue): #FIFO
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface but also inherits all methods from DLList

    def add(self, x : object):
        #for SLLQueue:
        super().add(x)
        if self.max_deque.n == 0: #check if the list is empty
            self.max_deque.add_first(x) #if yes, add the value as the head [first] of the list

        elif x > self.max_deque.get_node(0).x: #compare the x with the max value of the maxdeque_list
            for i in range(self.max_deque.n-1): #if x is bigger, run in the n-maxdeque,
                self.max_deque.remove(0)#and remove the first character of the list until empty
            self.max_deque.add_first(x) #then add the first character
        else: #if the x is not bigger
            for i in range(1,self.max_deque.n+1): #then run from the 1 to and end of the list
                #print('i1:',i)
                if x > self.max_deque.get(self.max_deque.n -1): #compare with the last character
                    # print('i2:',i)
                    # print('self.max',i,self.max_deque.get(i))
                    self.max_deque.remove_last() #if the x is bigger than any value in the list, then add x in that position
            self.max_deque.add_last(x)


    def remove(self) -> object:
        """ removes and returns the element at the head of the max queue """
        if self.max_deque.n == 0 : #if the list is none, then raise the error
            raise IndexError()
        head = self.head.x #get the first character of the list, the head
        func = super().remove() #the remove for the queue list
        if func == self.max_deque.dummy.next.x: #compare with the head of the deque
            # self.max_deque.dummy.next: get the next value base on the head in the list
            self.max_deque.remove_first()
        return head


    def max(self):
        """ returns the maximum element stored in the queue """
        return self.max_deque.get(0)



'''
# mq= MaxQueue()
# mq.remove()
# print(mq)


# TESTER
mq = MaxQueue()
mq.add(3)
print('1')
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print('2')
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print('3')
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print('4')
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print('5')
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print('6')
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print('7')
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print('8')
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print('9')
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print('10')
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print('11')
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print('12')
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print('13')
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print('size:',mq.size())
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
'''