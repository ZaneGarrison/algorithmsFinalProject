from binaryTree import *
from stack import *

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(i)
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

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
