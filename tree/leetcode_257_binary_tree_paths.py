# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children

#  preorder = [4, 2, 1, 3, 7, 6, 9]
#  inorder = [1, 2, 3, 4, 6, 7, 9]
from leetcode_105_construct_btree_thr_preorder_inorder import binary_tree
from leetcode_102_binary_tree_level_order_traversal import binary_tree_level

preorder = [4,2,1,14,12,3,7,6,9,8,11]
inorder = [14,1,12,2,3,4,6,7,8,9,11]
root = binary_tree().construct_btree(preorder, inorder)


import collections
class paths_binary_tree:
    level_order = collections.defaultdict(list)
    paths = list()
    def get_level_order(self, root):
        stacks = list()
        stacks.append(root)
        while len(stacks) != 0:
            node = stacks.pop(0)
            if node.left is not None:
                stacks.append(node.left)
                self.level_order[node.value].append(node.left.value)
            if node.right is not None:
                stacks.append(node.right)
                self.level_order[node.value].append(node.right.value)


    def tree_parent(self, root, value):
        if value == root.value:
            return
        for p, c in self.level_order.items():
            if value in c:
                self.paths.append(p)
                break
        self.tree_parent(root,p)

    def tree_paths(self, root, value):
        self.paths.append(value)
        self.tree_parent(root, value)


pbt = paths_binary_tree()
pbt.get_level_order(root)
print(pbt.level_order)
pbt.tree_paths(root, 11)
print(list(reversed(pbt.paths)))
pbt.paths = []
pbt.tree_paths(root, 14)
print(list(reversed(pbt.paths)))

