# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.

# Boundary includes left boundary leaves, and right boundary in order without duplicate nodes.
from leetcode_105_construct_btree_thr_preorder_inorder import binary_tree
from leetcode_102_binary_tree_level_order_traversal import binary_tree_level

preorder = [4,2,1,14,12,3,7,6,9,8,11]
inorder = [14,1,12,2,3,4,6,7,8,9,11]
btree_root = binary_tree().construct_btree(preorder, inorder)

class boundary_tree:
    left_boundary_arr = []
    leaves = []
    right_boundary_arr = []

    def get_all_leaves(self, root):
        if root is None:
            return True
        res_left = self.get_all_leaves(root.left)
        res_right = self.get_all_leaves(root.right)
        if res_left and res_right:
            self.leaves.append(root.value)

    def get_leaves_arr(self):
        return self.leaves

    def get_left_boundary(self, root):
        stack = list()
        if root is None:
            return True
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            self.left_boundary_arr.append(node.value)
            if node.left is not None:
                stack.append(node.left)
            elif node.right is not None:
                stack.append(node.right)
            else:
                break

    def get_left_boundary_arr(self):
        return self.left_boundary_arr

    def get_right_boundary(self, root):
        stack = list()
        if root is None:
            return True
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            self.right_boundary_arr.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            elif node.left is not None:
                stack.append(node.left)
            else:
                break

    def get_right_boundary_arr(self):
        return self.right_boundary_arr

    def get_btree_boundary(self, root):
        self.get_left_boundary(root)
        self.get_right_boundary(root)
        self.get_all_leaves(root)
        return self.left_boundary_arr + self.leaves[1:] + list(reversed(self.right_boundary_arr))[1:-1]

boundaryt = boundary_tree()
print(boundaryt.get_btree_boundary(btree_root))





