#Given two nodes of a binary tree p and q, return their lowest common ancestor(LCA)
#Each node will have a reference to its parent node.

#Example 1:
#                   3
#         5                  1
#    6          2       0         8
#           7       4

class Node:
    val = 0
    left = None
    right = None
    parent = None

    def __init__(self, val=0):
        self.val = val


class Solutions:
    def common_ancestor(self, root:'Node', p:'Node', q:'Node'):
        a = p
        b = q

        while a != b:
            if a != None:
                print('a = ', a.val)
                a = a.parent
            else:
                a = q
                print('a = q, a.val', a.val)
            if b != None:
                print('b = ', b.val)
                b = b.parent
            else:
                b = p
                print('b = p, b.val', b.val)

        if a == b:
            print('common ancestor is', a.val)
            return a
        else:
            print('non common ancestor')

rootnode = Node(3)
p =rootnode.left = Node(5)
rootnode.right = Node(1)

rootnode.left.parent = rootnode
rootnode.right.parent = rootnode

p = rootnode.left.left = Node(6)
rootnode.left.right = Node(2)

rootnode.left.left.parent = rootnode.left
rootnode.left.right.parent = rootnode.left

rootnode.left.right.left = Node(7)
q = rootnode.left.right.right = Node(4)

rootnode.left.right.left.parent = rootnode.left.right
rootnode.left.right.right.parent = rootnode.left.right

mysolution = Solutions()
LCAofPandQ = mysolution.common_ancestor(rootnode, p, q)
