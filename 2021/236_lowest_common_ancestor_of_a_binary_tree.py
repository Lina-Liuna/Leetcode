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
    def lowestCommonAncestor(self, root:'Node', p:'Node', q:'Node'):
        if root == None:
            print('first root none')
            return
        if root.val == p.val or root.val == q.val:
            print("catch, root.val'", root.val)
            return root
        print("root.val = ",root.val)
        print("travel root.val = ", root.val, 'left tree')
        left = self.lowestCommonAncestor(root.left, p,q)
        print("travel root.val = ", root.val, 'right tree')
        right = self.lowestCommonAncestor(root.right, p,q)
        if left is None:
            if right is not None:
                # the case that p/q is root and q/p is in the p/q's left tree
                print("return right root = ", root.val, "right is not none", right.val)
            else:
                # travel the leave
                print('return none')
            return right
        elif right is None:
            if left is not None:
                # the case that p/q is root and q/p is in the p/q's right tree
                print("return left root = ", root.val, "left is not none ", left.val)
            else:
                # travel the leave
                print('return none')
            return left
        else:
            #the case that p and q are not the parent / child related.
            print("root.val = ", root.val,"root left and right are not none", root.val, "return root")
            return root



rootnode = Node(3)
p = rootnode.left = Node(5)
rootnode.right = Node(1)

rootnode.left.left = Node(6)
q = rootnode.left.right = Node(2)
rootnode.left.right.left = Node(7)
rootnode.left.right.right = Node(4)

rootnode.right.left = Node(0)
rootnode.right.right = Node(8)

rootnode.left.right.left.left = Node(9)
rootnode.left.right.left.right = Node(12)
rootnode.left.right.right.left = Node(11)
rootnode.left.right.right.right = Node(15)
#q = Node(20)
mysolution = Solutions()
LCAofPandQ = mysolution.lowestCommonAncestor(rootnode,p,q)
if(LCAofPandQ != None):
    print(LCAofPandQ.val)