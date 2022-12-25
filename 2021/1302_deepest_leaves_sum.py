#Given the root of a binary tree, return the sum of values of its deepest leaves.
#           1
#       2       3
#    4     5       6
# 7                    8

#input: root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]
#Output: 15
import math

class BinaryTree:
    leavesArray = []
    def getleaves(self, root):
        for index in range(0, len(root)):
            if index == 0:
                leftnode = 1
                rightnode = leftnode + 1
            else:
                leftnode = (index << 1) + 1
                rightnode = leftnode + 1
            print(index, leftnode, rightnode, root[index], "True")
            if leftnode < len(root) and root[leftnode] == None and root[rightnode] == None:
                self.leavesArray.append(root[index])
                print("leaves")
    def getdepth(self,root):
        rootlength = len(root) - 1
        print(rootlength, bin(rootlength), len(bin(rootlength)), bin(rootlength)[1])
        depth = len(bin(rootlength)) - 2
        if depth == 0:
            print("root tree has only one item")
        elif depth != bin(rootlength).count("1"):
            depth = depth - 1
        #print(depth)
        return depth

    def depthestleavessum(self, root):
        depth = self.getdepth(root)
        sum = 0
        startIndex = int(math.pow(2, depth) - 1)
        #print(startIndex)
        for leave in root[startIndex:]:
            if leave != None:
                #print(leave)
                sum = sum + leave
        return sum

myBinaryTree = BinaryTree()
root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
print(myBinaryTree.depthestleavessum(root))
root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
print(myBinaryTree.depthestleavessum(root))

