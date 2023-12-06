import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1



def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2*(i+1)



def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """

    return (i-1)//2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()

        self.a[self.n] =x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError("Cannot remove from the empty heap.")
        x = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self._trickle_down_root()

        # if 3 * self.n < len(self.a):
        #     self._resize()
        return x

    def depth(self, u) -> int:
        if u not in self.a:
            raise ValueError(f"{u} not found in binary tree.")
        v = 0
        value_list = []
        for t in range(self.n):
            value_list.append(self.a[t])

        current_node = value_list.index(u)

        while current_node != 0:
            current_node = parent(current_node)
            v += 1
        return v

    def height(self) -> int:
        return int(math.log2(self.n))

    def bf_order(self) -> list:
        return list(self.a[0:self.n])

    def in_order(self) -> list:
        return self._in_order(0)

    def _in_order(self,i) -> list:
        value_list = []
        if left(i) < self.n:
            value_list.extend((self._in_order(left(i))))
        value_list.append(self.a[i])
        if right(i) < self.n:
            value_list.extend((self._in_order(right(i))))
        return value_list

    def post_order(self) -> list:
        return self._post_order(0)

    def _post_order(self, i) -> list:
        value_list = []
        if left(i) < self.n:
            value_list.extend(self._post_order(left(i)))
        if right(i) < self.n:
            value_list.extend(self._post_order(right(i)))
        value_list.append(self.a[i])
        return value_list


    def pre_order(self) -> list:
        return self._pre_order(0)

    def _pre_order(self, i):
        value_list = []
        value_list.append(self.a[i])
        if left(i) < self.n:
            value_list.extend(self._pre_order(left(i)))
        if right(i) < self.n:
            value_list.extend(self._pre_order(right(i)))
        return value_list

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i],self.a[p_idx] = self.a[p_idx],self.a[i]
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        resized_array = _new_array(max(1,2 * self.n))
        for i in range(0, self.n):
            resized_array[i] = self.a[i]
        self.a = resized_array

    def _trickle_down_root(self):
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        while (i <= self.n and l_idx <= self.n and r_idx <= self.n) and (
                self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
            if self.a[l_idx] <= self.a[r_idx]:
                min_idx = l_idx
            else:
                min_idx = r_idx

            self.a[i], self.a[min_idx] = self.a[min_idx],self.a[i]
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)


    def __str__(self):
            return str(self.a[0:self.n])


# heap = BinaryHeap()
# heap.add(5)
# heap.add(20)
# heap.add(30)
# heap.add(38)
# heap.add(35)
# heap.add(37)
# heap.add(52)
# heap.add(40)
# heap.add(42)
# print(list(heap.bf_order()))



