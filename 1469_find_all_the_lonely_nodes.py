#In a binary tree, a lonely node is a node that is the only child of its parent node.
#The root of the tree is not lonely because it does not have a parent node.
#Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree.
#Return the list in any order.

#Example 1:
#             1
#       2            3
#             4

#Input: root = [1,2,3,null, 4]
#Output:[4]

class Node:
    val = 0
    leftchild = None
    rightchild = None

    def __init__(self, val=0):
        self.val = val


    def midorder(self, root:'Node'):
        if root == None:
            return
        print(root.val)
        if root.leftchild != None:
            self.midorder(root.leftchild)
        if root.rightchild != None:
            self.midorder(root.rightchild)
class Solutions:
    ans = []
    def lonelychild(self, root:'Node'):
        if root == None:
            return
        if root.leftchild != None:
            if root.rightchild == None:
                self.ans.append(root.leftchild.val)
            self.lonelychild(root.leftchild)

        if root.rightchild != None:
            if root.leftchild == None:
                self.ans.append(root.rightchild.val)
            self.lonelychild(root.rightchild)

    def traverselonelychild(self):
        print(self.ans)




root = [1,2,3,None, 4]
root = [11,99,88,77,None,None,66,55,None,None,44,33,None,None,22]
roottree = Node(11)
roottree.leftchild = Node(99)
roottree.leftchild.leftchild = Node(77)
roottree.leftchild.rightchild = None
roottree.leftchild.leftchild.leftchild = Node(55)
roottree.leftchild.leftchild.rightchild = None
roottree.leftchild.leftchild.leftchild.leftchild = Node(33)
roottree.leftchild.leftchild.leftchild.rightchild = None
roottree.rightchild = Node(88)
roottree.rightchild.rightchild = Node(66)
roottree.rightchild.rightchild.rightchild = Node(44)
roottree.rightchild.rightchild.leftchild = None
roottree.rightchild.leftchild = None
roottree.rightchild.rightchild.rightchild.rightchild = Node(22)
roottree.rightchild.rightchild.rightchild.leftchild = None

mySolution = Solutions()
mySolution.lonelychild(roottree)
mySolution.traverselonelychild()





