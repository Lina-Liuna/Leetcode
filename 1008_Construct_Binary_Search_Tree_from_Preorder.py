# Given an array of integer preorder, which represents the preorder traversal of a BST(binary search tree),
# construct the tree and return it's root.

class Node:
    data = 0
    left = None
    right = None

    def __int__(self, val):
        self.data = val


class BTree:
    root = None

    def construct_BTree(self, preorder_arr, start, end):
        root_node = Node(preorder_arr[start])
        if start == 0:
            self.root = root_node
        if end >= len(preorder_arr):
            return self.root
        # root_node.left = self.construct_BTree(preorder_arr, start + 1, end)
        # root_node.right = self.construct_BTree(preorder_arr, )

