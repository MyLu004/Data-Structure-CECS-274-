import os

import Calculator
import BookStore
import BinaryTree
import BinarySearchTree
import ChainedHashTable
import DLList


def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable with values
        3 Print expression with values
        4 Evaluate expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")

        elif option == "2":
            cont = True
            while cont != False:
                variable = input('Enter a variable: ')
                value = input('Enter its value: ')
                value = float(value)
                calculator.set_variable(variable,value) #imply k,v | variable:k , value: v
                answer = input('Enter another variable? Y/N:')
                if answer == "N":
                    cont = False

        elif option == "3":
            expression = input('Introduce the mathematical expression: ')
            if calculator.matched_expression(expression):
                calculator.print_expression(expression)
            else:
                print('Invalid expression')

        elif option == "4":
            expression = input("Enter the expression: ")
            print_exp = calculator.print_expression(expression)
            error = False
            for value in print_exp:
                if value.isalpha():
                    error = True
                    print("Result: Error - Not all variable values are defined.")
                    break
            if not error:
                print(f"Evaluating expression: {print_exp}")
                print(f'Result: {calculator.evaluate(expression)}')

                # print("Evaluating expression:", end=" ")
                # print(c.print_expression(expression))
                # print("\n\nResult:", c.evaluate(expression))


        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            #file_name = input("Introduce the name of the file: ")
            file_name = "books.txt"
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == "6":
            bookStore.getCartBestSeller()
        elif option == "7":
            val = input('enter book key:')
            bookStore.addBookByKey(val)
        elif option == "8":
            prefix = input("Introduce the prefix: ")
            title = bookStore.addBookByPrefix(prefix)
            if title is not None:
                print(f'Added first matched title: {title}')
            else:
                print("Error: Prefix was not found.")
        elif option == "9":
            file_name = "books.txt"
            bookStore.loadCatalog(file_name)

            infix = str(input("Enter infix: "))
            structure = int(input("Enter structure (1 or 2): "))
            max_value = int(input("Enter max number of titles: "))
            bookStore.bestsellers_with(infix,structure,max_value)
        elif option == "10":
            print('Choose an algorithm:\n'
                  '\t1 - Merge Sort\n'
                  '\t2 - Quick Sort (first element pivot)\n'
                  '\t3 - Quick Sort (random element pivot\n')
            selection = int(input('Your selection: '))
            if bookStore.sort_catalog(selection) is False:
                print("Invalid algorithm")

        elif option == "11":
            amount = int(input("Enter the  number of books to display: "))
            bookStore.display_catalog(int(amount))






def menu_palindrome_test():
    val = input('Enter a word/phrase:')
    d = DLList.DLList()
    for char in val.lower(): #lowercase all characters
        if char.isalpha():
            d.append(char)

    if d.isPalindrome() == True:
        print('Result: PPalindrome')
    else:
        print(' Result: Not a palindrome')


    ''' 
        Add the menu options when needed
        '''


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        4 Evaluate expression
        0 Exit/Quit
        """)
        option = input()
        #option = 2

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            menu_palindrome_test()

if __name__ == "__main__":
    main()



