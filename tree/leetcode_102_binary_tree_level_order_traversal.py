# Given the root of a binary tree, return the level order traversal of its nodes' values(from left to right,
# level by level)

#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[9,20],[15,7]]

import leetcode_105_construct_btree_thr_preorder_inorder
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
btree = leetcode_105_construct_btree_thr_preorder_inorder.binary_tree()
btree_root = btree.construct_btree(preorder, inorder)

class binary_tree_level:
    level_order = list()
    stack = list()
    def level_order_traversal(self, root):
        self.stack.append(root)
        self.level_order.append([root.value])
        while len(self.stack) != 0:
            children = list()
            node = self.stack.pop()
            if node.left is not None:
                children.append(node.left.value)
                self.stack.append(node.left)
            if node.right is not None:
                children.append(node.right.value)
                self.stack.append(node.right)
            if node.left is not None or node.right is not None:
                self.level_order.append(children)

btl = binary_tree_level()
btl.level_order_traversal(btree_root)
print(btl.level_order)


