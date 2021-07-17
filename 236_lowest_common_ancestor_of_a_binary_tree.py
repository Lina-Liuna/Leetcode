#Given a binary tree, find the lowest common ancestor(LCA) of two given nodes in the tree.

#Example:

#                   3
#         5                  1
#    6          2       0         8
#           7       4
#        9     12   11  15
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Output: 3

class Node:
    val = 0
    left = None
    right = None

    def __init__(self, val=0):
        self.val = val

class Solutions:
    def lowestCommonAncestor(self, root:'Node', p:'Node', q:'Node', level):
        if root == None:
            return
        if root.val == p.val or root.val == q.val:
            print("catch, level = ", level, 'root.val', root.val)
            return root
        left = self.lowestCommonAncestor(root.left, p,q, level + 1)
        right = self.lowestCommonAncestor(root.right, p,q, level + 2)
        if left is None:
            if right is not None:
                print("return right root = ", root.val, "right is not none", right.val)
            return right
        elif right is None:
            if left is not None:
                print("return left root = ", root.val, "left is not none ", left.val)
            return left
        else:
            print("level = ", level, "root.val = ", root.val,"root left and right are not none", root.val, "return root")
            return root



rootnode = Node(3)
rootnode.left = Node(5)
rootnode.right = Node(1)

rootnode.left.left = Node(6)
rootnode.left.right = Node(2)
rootnode.left.right.left = Node(7)
rootnode.left.right.right = Node(4)

rootnode.right.left = Node(0)
rootnode.right.right = Node(8)

q = rootnode.left.right.left.left = Node(9)
rootnode.left.right.left.right = Node(12)
p = rootnode.left.right.right.left = Node(11)
rootnode.left.right.right.right = Node(15)

mysolution = Solutions()
LCAofPandQ = mysolution.lowestCommonAncestor(rootnode,p,q, 0)
print(LCAofPandQ.val)