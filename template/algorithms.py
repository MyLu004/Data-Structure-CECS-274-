"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):

    for i in range (len(a)):
        if a[i] == x:
            return i
    return None


def binary_search(a: List, x):
    begin_idx = 0
    end_idx = len(a)-1

    while begin_idx <= end_idx:
        midpoint = begin_idx +(end_idx - begin_idx)//2
        midpoint_value = a[midpoint]

        if midpoint_value == x: #return the value if found
            return midpoint
        elif x < midpoint_value:
            end_idx = midpoint - 1
        else:
            begin_idx = midpoint + 1

    return None



def _merge(a0: List, a1: List, a: List): #a0: left_arr, #a1: right_arr, #a:whole_arr
    i0 = 0 #idx for a0 [left]
    i1 = 0 #idx for a1 [right]
    k = 0
    while i0 < len(a0) and i1 < len(a1):
        if a0[i0] <= a1[i1]:
            a[k] = a0[i0]
            i0 = i0 + 1
        else:
            a[k] = a1[i1]
            i1 = i1 + 1
        k = k+1
    while i0 < len(a0):
        a[k] = a0[i0]
        i0 += 1
        k += 1
    while i1 < len(a1):
        a[k] = a1[i1]
        i1 = i1 + 1
        k = k +1
    return a



def merge_sort(a: List):
    if len(a) <= 1:
        return a #already sorted

    midpoint = len(a)//2
    a0 = a[0:midpoint]
    a1 = a[midpoint:len(a)]

    merge_sort(a0) #left
    merge_sort(a1) #right
    return _merge(a0,a1,a) #merge



def _quick_sort_f(a: List, start, end):
    if start < end:
        p = _partition_f(a, start, end)
        _quick_sort_f(a, start, p-1)
        _quick_sort_f(a, p+1, end)

def _quick_sort_r(a: List, start, end):
    if start < end:
        p = _partition_r(a, start, end)
        _quick_sort_r(a, start, p - 1)
        _quick_sort_r(a, p + 1, end)

def _partition_f(a: List, start, end):
    l = start +1
    r = end
    pivot = a[start]

    while l < r:
        while l <= end and a[l] <= pivot:
            l = l + 1
        while r > start and a[r] > pivot:
            r = r -1
        if l <= r:
            a[l],a[r] = a[r],a[l]
    if a[r] <= pivot:
        a[r],a[start] = a[start],a[r]

    return r

def _partition_r(a: List, start, end):
    l = start +1
    r = end
    ran_pivot = random.randint(start,end)
    a[start],a[ran_pivot] = a[ran_pivot],a[start]
    pivot = a[start]

    while l < r:
        while l <= end and a[l] <= pivot:
            l = l + 1
        while r > start and a[r] > pivot:
            r = r -1
        if l <= r:
            a[l],a[r] = a[r],a[l]
    if a[r] <= pivot:
        a[r],a[start] = a[start],a[r]

    return r


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, len(a)-1)
    else:
        _quick_sort_f(a, 0, len(a)-1)


# if __name__ == "__main__":
#     val1 = [-20, -15, -13, -21, 16, -15, -10, 21, -21, 1, -10, 11]
#     val2 = [-12, 13, -3, -22, -16, 23, 24, -18, -2, 3, -21, 12]
#     # quick_sort(val1,False)
#     # print('the f_quicksort',val1)
#     #
#     # quick_sort(val2,True)
#     # print('the r_quicksort',val2)
#     merge_sort(val1)
#     # print(val1)
#     print (3 > 3)
#     print(3 < 3)