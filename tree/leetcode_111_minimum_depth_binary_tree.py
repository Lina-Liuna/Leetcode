# Given a binary tree, find its minimum depth
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.

import leetcode_105_construct_btree_thr_preorder_inorder
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
btree = leetcode_105_construct_btree_thr_preorder_inorder.binary_tree()
btree_root = btree.construct_btree(preorder, inorder)

class min_depth_btree:
    def minimum_depth_binary_tree(self, root):
        if root is None:
            return 0
        left_height = self.minimum_depth_binary_tree(root.left)
        right_height = self.minimum_depth_binary_tree(root.right)
        return 1 + min(left_height, right_height)


t = min_depth_btree()
depth = t.minimum_depth_binary_tree(btree_root)
print(depth)
