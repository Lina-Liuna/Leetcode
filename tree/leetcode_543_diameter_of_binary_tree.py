# Given the root of a binary tree, return the length of the diameter of the tree
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# we can calculate each node's sum(left + right), and the max of sum(left+ right) is the diameter

import leetcode_105_construct_btree_thr_preorder_inorder
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
btree = leetcode_105_construct_btree_thr_preorder_inorder.binary_tree()
btree_root = btree.construct_btree(preorder, inorder)


import collections

class diameter_binary_tree:
    diameters = collections.defaultdict(list)
    def depth_sum(self, node):
        if node is None:
            return 0
        depth_left = self.depth_sum(node.left)
        depth_right = self.depth_sum(node.right)
        self.diameters[node.value] = [depth_left, depth_right]
        return 1 + max(depth_left, depth_right)

    def diameter(self, root):
        if root is None:
            return 0
        self.depth_sum(root)
        max = 0
        for k in self.diameters:
            if max < sum(self.diameters[k]):
                max = sum(self.diameters[k])

        return max

dbt = diameter_binary_tree()
diameeter_num = dbt.diameter(btree_root)
print(dbt.diameters)
print(diameeter_num)






