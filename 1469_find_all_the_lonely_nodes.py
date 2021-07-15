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
    nodelist = []
    def gennodelist(self, list):
        for index, item in enumerate(list):
            self.nodelist.append(Node(item))
            print(self.nodelist[index].val)
    def binaryTree(self):
        for index, node in enumerate(self.nodelist):
            bitleftchildindex = bin(index) + "1"
            leftchildindex = int(bitleftchildindex, 2)
            if leftchildindex < len(self.nodelist):
                print(node.val, leftchildindex, self.nodelist[leftchildindex].val)
                node.leftchild = self.nodelist[leftchildindex]
            if leftchildindex + 1 < len(self.nodelist):
                print(node.val, leftchildindex + 1, self.nodelist[leftchildindex + 1].val)
                node.rightchild = self.nodelist[leftchildindex + 1]
        return self.nodelist[0]
    def lonelychild(self, root:'Node'):
        if root == None:
            return
        if root.leftchild != None:
            self.lonelychild(root.leftchild)
            if root.rightchild != None:
                print("lonelychild", root.val)
        if root.rightchild != None:
            self.lonelychild(root.rightchild)
            if root.leftchild != None:
                print("lonelychild", root.val)



root = [1,2,3,None, 4]
mysolution = Solutions()
mysolution.gennodelist(root)
mybintree = mysolution.binaryTree()
mybintree.midorder(mybintree)
mysolution.lonelychild(mybintree)





