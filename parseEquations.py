from binaryTree import *
from stack import *

def buildParseTree(inputEquation):
    equation = inputEquation.split()
    p_stack = Stack()
    bTree = BinaryTree('')
    p_stack.push(bTree)
    currentTree = bTree

    for i in equation:
        if i == '(':
            currentTree.insertLeft('')
            p_stack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            p_stack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = p_stack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(i)
            parent = p_stack.pop()
            currentTree = parent

    return bTree

equation = input("Enter an equation with explicit parentheses:\n ex: ( ( ( 1 + 2 ) * 3 ) - 4 )\n")
pt = buildParseTree(equation)
print("Preorder Printing:")
pt.preorder()
print()
print("Inorder Printing:")
pt.inorder()
print()
print("Postorder Printing:")
pt.postorder()
