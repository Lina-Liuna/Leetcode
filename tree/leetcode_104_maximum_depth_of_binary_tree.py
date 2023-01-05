# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#Input: root = [3,9,20,null,null,15,7]
#Output: 3

import leetcode_105_construct_btree_thr_preorder_inorder
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
btree = leetcode_105_construct_btree_thr_preorder_inorder.binary_tree()
btree_root = btree.construct_btree(preorder, inorder)

class max_depth_btree:
    def maximum_depth_binary_tree(self, root):
        if root is None:
            return 0
        left_height = self.maximum_depth_binary_tree(root.left)
        right_height = self.maximum_depth_binary_tree(root.right)
        return 1 + max(left_height, right_height)


t = max_depth_btree()
depth = t.maximum_depth_binary_tree(btree_root)
print(depth)
