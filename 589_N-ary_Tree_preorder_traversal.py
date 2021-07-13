#Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
#Nary-Tree input serialization is represented in their level order traversal.
#Each group of children is separated by the null value

#                1
#      3         2          4
#  5       6

#Input: root = [1,null,3,2,4,null,5,6]
#Output: [1,3,5,6,2,4]

class Node:
    val = 0
    children = []
    def __init__(self, val):
        self.val = val
        self.children = []

    def preorder(self, root:'Node'):
        res = []
        if not root:return
        #print(root.val)
        res.append(root.val)
        for child in root.children:
            res.extend(root.preorder(child))
        return res

root = Node(1)
root.children.append((Node(3)))
root.children.append((Node(2)))
root.children.append((Node(4)))
root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))
print(root.preorder(root))