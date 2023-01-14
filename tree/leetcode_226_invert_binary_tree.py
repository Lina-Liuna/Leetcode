# Given the root of a binary tree, invert the tree, and return its root.
#Input: root = [4,2,7,1,3,6,9]
#Output: [4,7,2,9,6,3,1]

from leetcode_105_construct_btree_thr_preorder_inorder import binary_tree
from leetcode_102_binary_tree_level_order_traversal import binary_tree_level

preorder = [4, 2, 1, 3, 7, 6, 9]
inorder = [1, 2, 3, 4, 6, 7, 9]
root = binary_tree().construct_btree(preorder, inorder)
btl = binary_tree_level()
btl.level_order = []
level_order = btl.level_order_traversal(root)
print(level_order)


class binary_tree_invert:
    def invert_btree(self, root):
        if root is not None:
            swap = root.left
            root.left = root.right
            root.right = swap
            self.invert_btree(root.left)
            self.invert_btree(root.right)

bti = binary_tree_invert()
bti.invert_btree(root)
btl.level_order = []
level_order = btl.level_order_traversal(root)
print(level_order)