#Given the root of a binary tree, return the lowest common ancestor of two given nodes, p and q.
#If either node p or q does not exist in the tree, return null.
#All values of the node in the tree are unique.

#Example 1:
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
    def ischild(self, root:'Node', p:'Node'):
        if root == None:
            return False
        if root.val == p.val:
            return True
        flagl = self.ischild(root.left, p)
        flagr = self.ischild(root.right,p)
        if flagr == True or flagl == True:
            return True



class Solution:
    counter = 0
    def lowestcommonancestor(self, root:'Node', p:'Node', q:'Node',level):
        if root is None:
            return None
        print('root.val', root.val)
        #if self.pFlag == True and self.qFlag == True:
        left = self.lowestcommonancestor(root.left, p, q, level)
        right = self.lowestcommonancestor(root.right, p, q, level)
        if root.val == p.val or root.val == q.val:
            print("catch, root.val'", root.val)
            self.counter = self.counter + 1
            return root
        elif left is None:
            if right is not None:
                print("return right root = ", root.val, "right is not none", right.val)
            else:
                print('return none')
            return right
        elif right is None:
            if left is not None:
                print("return left root = ", root.val, "left is not none ", left.val)
            else:
                print('return none')
            return left
        else:
            print("root.val = ", root.val, "root left and right are not none", root.val, "return root")
            return root


rootnode = Node(3)
p =rootnode.left = Node(5)
rootnode.right = Node(1)

rootnode.left.left = Node(6)
rootnode.left.right = Node(2)
rootnode.left.right.left = Node(7)
rootnode.left.right.right = Node(4)

rootnode.right.left = Node(0)
rootnode.right.right = Node(8)

rootnode.left.right.left.left = Node(9)
rootnode.left.right.left.right = Node(12)
rootnode.left.right.right.left = Node(11)
q = rootnode.left.right.right.right = Node(15)
#q = Node(20)
mysolution = Solution()
LCAofPandQ = mysolution.lowestcommonancestor(rootnode, p, q, 0)
if(LCAofPandQ != None and mysolution.counter == 2):
    print(LCAofPandQ.val)
else:
    print('not found the lowest common ancestor')
