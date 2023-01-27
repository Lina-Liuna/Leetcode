# Given a binary tree where all the right nodes are either leaf nodes with a sibling or empty, flip it upside down and
# turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
import collections
from leetcode_105_construct_btree_thr_preorder_inorder import binary_tree
from leetcode_102_binary_tree_level_order_traversal import binary_tree_level

preorder = [1,2,4,5,3]
inorder = [4,2,5,1,3]
btree_root = binary_tree().construct_btree(preorder, inorder)


class UpsideDownTree:
    left_boundary_nodes = collections.defaultdict(list)
    udtree_root = None

    def get_left_boundary_nodes(self, root):
        if root is None:
            return True
        self.left_boundary_nodes[root] = [root.left, root.right]
        res = self.get_left_boundary_nodes(root.left)

    def upside_down_tree(self):
        res = collections.OrderedDict(reversed(self.left_boundary_nodes.items()))
        for root, [left, right] in res.items():
            if left is None:
                self.udtree_root = root
            if left is not None:
                print(left.value)
                left.left = right
                left.right = root




udtree = UpsideDownTree()
udtree.get_left_boundary_nodes(btree_root)
print(udtree.left_boundary_nodes.keys())
udtree.upside_down_tree()
