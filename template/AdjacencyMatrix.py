from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        # todo
        if i <= 0 and j >= self.n:
            raise IndexError
        else:
            self.adj[i][j] = True

    def remove_edge(self, i : int, j : int):
        if i <= 0 and j >= self.n:
            raise IndexError

        if self.adj[i][j] == 0: #this edge already remove, node
            return False
        else: #remove this edge, node
            self.adj[i][j] = 0
            return True

    def has_edge(self, i : int, j: int) ->bool:
        if i <= 0 and j >= self.n:
            raise IndexError
        return self.adj[i][j] #get the node info

    def out_edges(self, i) -> List:
        edges = []
        for j in range(len(self.adj[i])): #getting the edge depend on the i_list
            if self.adj[i][j] == 1:
                edges.append(j)
        return edges

    def in_edges(self, j) -> List:
        edges = []
        for i in range(len(self.adj[j])): #getting the edge depend on the j_list
            if self.adj[i][j] == 1:
                edges.append(i)
        return edges

    def bfs(self, r : int):
        traversal = []
        seen = [False] * self.n
        q = ArrayQueue.ArrayQueue()
        q.add(r) #add the initial value
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
        traversal = []
        s = ArrayStack.ArrayStack()
        seen = [False] * self.n

        s.push(r)

        while s.n != 0:
            current = s.pop()
            if not seen[current]:
                traversal.append(current)
                seen[current] = True
                neighbors = self.out_edges(current)

                for neighbors in reversed(neighbors):
                    if not seen[neighbors]:
                        s.push(neighbors)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def size(self) -> int:
        return self.n

