# Given a binary tree, determine if it is height-balanced
# For this problem, a height-balanced binary tree is defined as:
# A binary tree in which is the left and right subtree of every node differ in height by nor more than 1
import leetcode_105_construct_btree_thr_preorder_inorder
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
btree = leetcode_105_construct_btree_thr_preorder_inorder.binary_tree()
btree_root = btree.construct_btree(preorder, inorder)

class Node:
    val = 0
    left = None
    right = None

class balanced_binary_tree:
    def binary_tree_height(self, root):
        if root is None:
            return 0
        left_height = self.binary_tree_height(root.left) + 1
        right_height = self.binary_tree_height(root.right) + 1
        return max(left_height, right_height)

    def is_balanced_binary_tree(self, root):
        if root is None:
            return True
        left_height = self.binary_tree_height(root.left)
        right_height = self.binary_tree_height(root.right)
        if abs(right_height - left_height) > 1:
            return False
        else:
            return True

bbt = balanced_binary_tree()
print(bbt.is_balanced_binary_tree(btree_root))
preorder = [3,9,20]
inorder = [20, 9, 3]
btree_root = btree.construct_btree(preorder, inorder)
print(bbt.is_balanced_binary_tree(btree_root))