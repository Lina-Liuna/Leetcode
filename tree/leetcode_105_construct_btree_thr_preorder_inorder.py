# Given two integer arrarys preorder and inorder where preorder is preorder traversal of a binary tree
# and inorder is the inorder traversal of the same tree, construct and return the binary tree
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
class Node:
    value = 0
    left = None
    right = None

    def __init__(self, val):
        self.value = val


class binary_tree:
    root: 'Node'

    def construct_btree(self, preorder_arr, inorder_arr):
        if len(inorder_arr) != 0:
            root = Node(preorder_arr.pop(0))
            root_index = inorder_arr.index(root.value)
            root.left = self.construct_btree(preorder_arr, inorder_arr[:root_index])
            root.right = self.construct_btree(preorder_arr, inorder_arr[root_index + 1:])
            return root

    def print_btree(self, root):
        if root is not None:
            print(root.value)
            self.print_btree(root.left)
            self.print_btree(root.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

btree = binary_tree()
btree_root = btree.construct_btree(preorder, inorder)
btree.print_btree(btree_root)
