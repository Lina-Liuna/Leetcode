#Given a binary search tree(BST), find the lowest common ancestor(LCA) of two given nodes in the BST

#Example:

#                6
#         2             8
#     0      4        7    9
#          3    5


#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#6

class Node:
    val = 0
    left = None
    right = None

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solutions:
    def LCAofBST(self, root:'Node', p:'Node', q:'Node'):
        if root == None:
            return
        if root.val < p.val and root.val < q.val:
            root = self.LCAofBST(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            root = self.LCAofBST(root.left, p, q)
        return root

rootnode = Node(6)
rootnode.left = Node(2)
rootnode.right = Node(8)

rootnode.left.left = Node(0)
rootnode.left.right = Node(4)
rootnode.left.right.left = Node(3)
rootnode.left.right.right = Node(5)

rootnode.right.left = Node(7)
rootnode.right.right = Node(9)

p = Node(2)
q = Node(8)
mysolution = Solutions()
LCAofPandQ = mysolution.LCAofBST(rootnode, p, q)

print(LCAofPandQ.val)