import Book
import ChainedHashTable
import ArrayList
import ArrayQueue
import RandomQueue
#import DLList
#import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
#import AdjacencyList
import time
import MaxQueue
import algorithms

class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()
        #self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        #self.bookCatalog = DLList.DLList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                #self.bookIndices.add(key,self.bookCatalog.size()-1)
                self.sortedTitleIndices.add(title,self.bookCatalog.size()-1)
                #print('sorted:',self.sortedTitleIndices.add(title,self.bookCatalog.size()-1)

            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")



    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        #self.shoppingCart = ArrayQueue.ArrayQueue()
        self.shoppingCart = MaxQueue.MaxQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByKey(self,key):
        start_time = time.time()
        value = self.bookIndices.find(key)
        #print('value:',value)

        if value is not None:
            book = self.bookCatalog.get(value)
            self.shoppingCart.add(book)

        elif value is None:
            print('Book not found...')
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            #self.shoppingCart.add(s.rank)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    #def searchBookByInfix(self, infix: str):
    def searchBookByInfix(self, infix: str, cnt : int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string
        '''
        start_time = time.time()
        num = 0  # number if result
        for value in self.bookCatalog:
            if infix in value.title:
                print(value)
                num += 1
                if num == cnt:
                    break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")


    def getCartBestSeller(self):
        bestbook = self.shoppingCart.max()
        print('getCartBestSeller returned:')
        print(bestbook.title)

    def addBookByPrefix(self, prefix: str):
        start_time = time.time()
        val = self.sortedTitleIndices.finding_value(prefix)
        get = self.bookCatalog.get(val)
        if get.title[0:len(prefix)] == prefix and prefix != "":
            self.shoppingCart.add(get)
            print(f"Added first matched title: {get.title}")
        else:
            print("Prefix was not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByPrefix Completed in {elapsed_time} seconds")

    def bestsellers_with(self, infix, structure,n = 0):
        best_sellers = None
        if structure == 1: #Binary Search Tree
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2: #Binary Heap
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure")

        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()
                if structure == 1:
                    for book in self.bookCatalog:
                        if infix in book.title:
                            best_sellers.add(book.rank, book)
                    bag = best_sellers.in_order()
                    bag = bag [::-1]
                    if n == 0:
                        for book in bag:
                            print(book.v)
                    else:
                        num = 0
                        while num != n:
                            print(bag[num].v)
                            num += 1
                if structure == 2:
                    for book in self.bookCatalog:
                        if infix in book.title:
                            best_sellers.add(book.rank*-1)
                    ranking = []
                    for rank in range(best_sellers.size()):
                        ranking.append(best_sellers.remove()*-1)
                    bag = []
                    for rank in ranking:
                        for book in self.bookCatalog:
                            if book.rank == rank:
                                bag.append(book)
                    if n == 0:
                        for value in bag:
                            print(value)
                    else:
                        num = 0
                        while num != n:
                            print(bag[num])
                            num += 1

                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n} in {elapsed_time} seconds")

    def sort_catalog(self,s): #s: selection
        start_time = time.time()
        if s == 1:
            self.bookCatalog = algorithms.merge_sort(self.bookCatalog)
            elapsed_time = time.time() - start_time
            print(f"Sorted self.bookCatalog.size() books in {elapsed_time} seconds")
            return True
            pass
        elif s == 2:
            self.bookCatalog = algorithms.quick_sort(self.bookCatalog,False)
            elapsed_time = time.time() - start_time
            print(f"Sorted self.bookCatalog.size() books in {elapsed_time} seconds")
            return True
        elif s ==3:
            self.bookCatalog = algorithms.quick_sort(self.bookCatalog,True)
            elapsed_time = time.time() - start_time
            print(f"Sorted self.bookCatalog.size() books in {elapsed_time} seconds")
            return True
        else:
            return False

    def display_catalog(self,amount):
        count = 0
        while count < amount:
            print(self.bookCatalog[count])
            count += 1








# B = BookStore()
# B.loadCatalog("books.txt")
# B.sort_catalog(1)
# B.display_catalog(5)