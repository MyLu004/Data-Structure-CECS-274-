"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if i <= 0 and j >= self.n:
            raise IndexError()
        if not self.has_edge(i, j):
            self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        if i < 0 or j >= self.n:
            raise IndexError()
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        if i < 0 or j >= self.n:
            raise IndexError()
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return True
            return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, j) -> List:
        edges = ArrayList.ArrayList()
        for k in range(len(self.adj)):
            if self.has_edge(k,j):
                edges.append(k)
        return edges

    def bfs(self, r : int):
        # todo
        traversal = []
        seen = [False] * self.n
        q = ArrayQueue.ArrayQueue()
        q.add(r)  # add the initial value
        traversal.append(r)
        seen[r] = True
        while q.n != 0:
            current = q.remove()
            neighbors = self.out_edges(current)

            for jk in neighbors:
                if not seen[jk]:
                    q.add(jk)
                    traversal.append(jk)
                    seen[jk] = True

        return traversal

    def dfs(self, r : int):
        # todo
        traversal = [] #empty list of traversal
        s = ArrayStack.ArrayStack() #stack s
        seen = [False] * self.n #seen of n [boolean False]

        s.push(r) #push r[initial variable] in to stack

        while s.n != 0: #if stack not empty
            current = s.pop() #Temporary variable [return the first element from the list]
            if not seen[current]: #check for visited for the return variable [if not False = if true]
                traversal.append(current) #if not, append into the traversal
                seen[current] = True #set the remove variable true
                neighbors = self.out_edges(current) #list of indices of current

                for jk in reversed(neighbors):
                    if not seen[jk]:
                        s.push(jk)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

    def size(self) -> int:
        return self.n