import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import re
import operator
import BinarySearchTree



class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
        #self.dict = None

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for i in range(len(s)):
            if s[i] == '(':
                stack.push('(')
            if s[i] == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0 and True:
            return True
        else:
            return False

    def print_expression(self, exp:str):
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        everything_else = re.split('\w+', exp)
        # print('Chainedtable:',self.dict)
        for i in range(len(variables)):  # check for the variable value
            # self.dict.find(variables[i])
            replace_val = self.dict.find(variables[i])  # if find the value, get the it
            if replace_val == None:  # if not, just pass
                pass
            else:
                variables[i] = str(replace_val)  # then start replace the variable with value [replace_val]
        list = ''
        while len(variables) > 0 and len(everything_else) > 0:
            list += everything_else[0] + variables[0]
            del variables[0]
            del everything_else[0]
        while len(everything_else) > 0:
            list += everything_else[0]
            del everything_else[0]
        #print(list)
        return list

    def _build_parse_tree(self, exp: str) -> str:
        if not self.matched_expression(exp):
            raise SyntaxError('Match wrong')
        tokens = []
        i = 0
        while i < len(exp):
            current_token = ""
            if exp[i].isalnum() == False:
                current_token = exp[i]
                tokens.append(current_token)
                i += 1
                continue
            while exp[i].isalnum() == True:
                current_token += exp[i]
                i += 1
            tokens.append(current_token)

        #Sprint(tokens)

        t = BinaryTree.BinaryTree()
        t.r = t.Node()
        current = t.r
        #print('letter expression', exp)
        for token in tokens:
            node = t.Node()
            if token == "(":
                current = current.insert_left(node)
            elif token =="+" or token == "-" or token =="*" or token =="/":
                current.set_val(token)
                current.set_key(token)
                current = current.insert_right(node)
            elif token.isalnum():
                current.set_val(self.dict.find(token))
                current.set_key(token)
                current = current.parent
            elif token == ")":
                current = current.parent
        return t


    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        if root.left is not None and root.right is not None:
            func = op[root.k]
            return func(self._evaluate(root.left), self._evaluate(root.right))
        elif root.left is None and root.right is None:
            if root.v is not None:
                return root.v
            raise ValueError(f"Missing value for variable {root.k}")
        elif root.left is not None:
            return self._evaluate(root.left)
        else:
            raise self._evaluate(root.right)




# c = Calculator()
# expression = "((a+b)*(c+d))"
# c.set_variable('a', 3.94)
# c.set_variable('b', 9.64)
# c.set_variable('c', 6.03)
# c.set_variable('d', 6)
# print("Evaluating expression:", end=" ")
# print(c.print_expression(expression))
# #print("expression after the print_exp method: ",expression)
# print("\n\nResult:", c.evaluate(expression))



