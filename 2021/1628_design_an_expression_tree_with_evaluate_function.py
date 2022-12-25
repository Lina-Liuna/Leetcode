#Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents
#this expression.

#The class Node is an interface you should use to implement the binary expression tree.
#The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value
#You should not remove the Node class; however, you can modify it as you wish, and you cna define other classes
#to implement it if needed.

#Example 1:
#                 /
#         *               7
#      +      2
#   3     4

#input s = ["3","4","+","2","*","7","/"]
#Output: 2

class Node:
    val = ''
    leftchild = None
    rightchild = None

    def __init__(self, val, lc=None, rc=None):
        self.val = val
        self.leftchild = lc
        self.rightchild = rc

    def preorder(self, root:'Node'):
        if root.leftchild != None:
            self.preorder(root.leftchild)
        print(root.val)
        if root.rightchild != None:
            self.preorder(root.rightchild)


class Solution:

    def expressiontree(self, elist):
        operatorstack = []
        for item in elist:
            print(item)
            if item.isdigit() == True:
                operatorstack.append(Node(item))
            else:
                operNode = Node(item)
                operNode.rightchild = operatorstack.pop()
                operNode.leftchild = operatorstack.pop()
                operatorstack.append(operNode)
        return operatorstack.pop()

    def evaluate(self, root: 'Node'):
        if root.leftchild != None:
            leftval = int(self.evaluate(root.leftchild))
        if root.rightchild != None:
            rightval = int(self.evaluate(root.rightchild))
        if root.val == "+":
            return leftval + rightval
        elif root.val == "-":
            return leftval - rightval
        elif root.val == "*":
            return leftval * rightval
        elif root.val == "/":
            return leftval / rightval
        else:
            return int(root.val)

s = ["3","4","+","2","*","7","/"]
mysolution = Solution()
root = mysolution.expressiontree(s)
root.preorder(root)
print(mysolution.evaluate(root))
s = ["4","5","7","2","+","-","*"]
mysolution = Solution()
root = mysolution.expressiontree(s)
root.preorder(root)
print(mysolution.evaluate(root))
s = ["4","2","+","3","5","1","-","*","+"]
root = mysolution.expressiontree(s)
root.preorder(root)
print(mysolution.evaluate(root))



