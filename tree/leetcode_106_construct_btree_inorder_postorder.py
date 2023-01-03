# Given two integer inorder and postorder when inorder is the inorder traversal of a binary tree and
# postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Input: inorder = [8,9,5,3,15,20,7], postorder = [8, 5, 9,15,7,20,3]
# Output: [3,9,8,5,20,15,7]

class Node:
    data = 0
    left = None
    right = None

    def __init__(self, val):
        self.data = val


class BTree:
    def find_rightmost_in_postorder(self, postorder, inorder):
        rightmost_index = 0
        for item in inorder:
            if rightmost_index < postorder.index(item):
                rightmost_index = postorder.index(item)
        return rightmost_index

    def find_node_index_in_inorder(self, node_val, inorder):
        return inorder.index(node_val)

    def construct_BTree(self, postorder, inorder):
        if len(inorder) != 0:
            root_index_in_postorder = self.find_rightmost_in_postorder(postorder, inorder)
            root_data = postorder[root_index_in_postorder]
            root = Node(root_data)
            root_index_in_inorder = self.find_node_index_in_inorder(root_data, inorder)
            root.left = self.construct_BTree(postorder, inorder[:root_index_in_inorder])
            root.right = self.construct_BTree(postorder, inorder[root_index_in_inorder + 1:])
            return root

    def preorder_Btree(self, root):
        if root is not None:
            print(root.data)
            self.preorder_Btree(root.left)
            self.preorder_Btree(root.right)


inorder = [8, 9, 5, 3, 15, 20, 7]
postorder = [8, 5, 9, 15, 7, 20, 3]
btree = BTree()
root = btree.construct_BTree(postorder, inorder)
btree.preorder_Btree(root)

