# Given an array of integer preorder, which represents the preorder traversal of a BST(binary search tree),
# construct the tree and return it's root.

class Node:
    data = 0
    left = None
    right = None

    def __init__(self, val):
        self.data = val


class BSTree:
    def find_most_right_index_smaller_than_root(self, root_val, preorder):
        max_index = 0
        for item in preorder:
            if item <= root_val:
                max_index = preorder.index(item)
        return max_index

    def find_most_left_index_bigger_than_root(self, root_val, preorder):
        index = 0
        for item in preorder:
            if item > root_val:
                index = preorder.index(item)
                return index

    def construct_BST(self, preorder):
        if len(preorder) != 0:
            root = Node(preorder[0])
            left_index = self.find_most_right_index_smaller_than_root(root.data, preorder)
            right_index = self.find_most_left_index_bigger_than_root(root.data, preorder)
            if right_index is None:
                root.right = None
            else:
                root.right = self.construct_BST(preorder[right_index:])
            if left_index is None:
                root.left = None
            else:
                root.left = self.construct_BST(preorder[1:left_index + 1])
            return root

    def preorder_BST(self, root):
        if root is not None:
            print(root.data)
            self.preorder_BST(root.left)
            self.preorder_BST(root.right)


preorder = [8, 3, 1, 6, 4, 7, 15, 9, 20, 16]

bstree = BSTree()
root = bstree.construct_BST(preorder)
bstree.preorder_BST(root)
