# Given a binary tree root, a node X in the tree is named good if in the path from root to X are no nodes with a value
# greater than X.
# Return the number of good nodes in the binary tree.
import collections
from leetcode_105_construct_btree_thr_preorder_inorder import binary_tree
preorder = [3,9,8,5,20,15,7]
inorder = [8,9,5,3,15,20,7]
btree = binary_tree()
btree_root = btree.construct_btree(preorder, inorder)


class binarytree:
    ancestors = collections.defaultdict(list)

    def get_node_ancestor(self, root, target):
        if root is None:
            return False
        if root.value == target:
            return True
        left_result = self.get_node_ancestor(root.left, target)
        right_result = self.get_node_ancestor(root.right, target)
        if left_result or right_result:
            self.ancestors[target].append(root.value)
            return True
        return False

    def nodes_ancestors(self, node, root):
        if node is None:
            return 0
        self.get_node_ancestor(root, node.value)
        self.nodes_ancestors(node.left, root)
        self.nodes_ancestors(node.right, root)

    def check_if_largest_in_arr(self, n, arr):
        for a in arr:
            if n < a:
                return 0
        return 1

    def count_good_nodes(self):
        count = 0
        for d in self.ancestors:
            count = count + self.check_if_largest_in_arr(d, self.ancestors[d])
        return count


bt = binarytree()
bt.nodes_ancestors(btree_root, btree_root)
print(bt.ancestors)
good_nodes_num = bt.count_good_nodes()
print(good_nodes_num)