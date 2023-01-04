# Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.
import leetcode_105_construct_btree_thr_preorder_inorder


class binary_tree:
    def print_ancestors(self, root, target):
        if root is None:
            return False

        if root.value == target:
            return True

        left_result = self.print_ancestors(root.left, target)
        right_result = self.print_ancestors(root.right, target)
        if left_result or right_result:
            print(root.value, end=' ')
            return True
        return False

    def print_btree(self, root):
        if root is not None:
            print(root.value)
            self.print_btree(root.left)
            self.print_btree(root.right)


# preorder = [3,9,8,5,20,15,7]
r = leetcode_105_construct_btree_thr_preorder_inorder.btree_root

t = binary_tree()
t.print_ancestors(r, 5)
