# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values
# postorder is the postorder traversal of the sam tree, reconstruct and return the binary tree
# If there exist multiple answers, you can return any of them

# preorder = [8, 3, 1, 6, 4, 7, 15, 9, 20, 16]
# postorder = [1, 4, 7, 6, 3, 9, 16, 20, 15, 8]

class Node:
    data = 0
    left = None
    right = None

    def  __init__(self, val):
        self.data = val

class BTree:

    def find_left_children_max_index_in_postorder(self, val, postorder):
        for item in postorder:
            if val == item:
                return postorder.index(item)

    def find_left_children_max_index_in_preorder(self,preorder, postorder):
        max_index = 0
        for item in postorder:
            index = preorder.index(item)
            if index > max_index:
                max_index = index
        return max_index

    def find_right_child_index_in_preorder(self, val, preorder):
        for item in preorder:
            if val == item:
                return preorder.index(item)

    def get_right_children_in_preorder(self, val, preorder):
        index = self.find_right_child_index_in_preorder(val, preorder)
        return preorder[index:]

    def get_right_children_in_postorder(self, val, preorder, postorder):
        right_children_in_preorder = self.get_right_children_in_preorder(val, preorder)
        min_index = 2000
        for item in right_children_in_preorder:

            index = postorder.index(item)
            if index < min_index:
                min_index = index
        return postorder[min_index: min_index + len(right_children_in_preorder)]

    def get_left_children_in_postorder(self, val, postorder):
        index = self.find_left_children_max_index_in_postorder(val, postorder)
        return postorder[:index + 1]

    def get_left_children_in_preorder(self, val, preorder, postorder):
        left_children_post_order = self.get_left_children_in_postorder(val, postorder)
        index = self.find_left_children_max_index_in_preorder(preorder, left_children_post_order)
        return preorder[1:index+ 1]

    def construct_BTree(self, preorder, postorder ):
        if len(preorder) != 0:
            root = Node(preorder[0])
            if len(preorder) - 1 != 0 and len(postorder) != 0:
                left_child_data = preorder[1]
                left_children_preorder = self.get_left_children_in_preorder(left_child_data, preorder, postorder)
                left_children_postorder = self.get_left_children_in_postorder(left_child_data, postorder)
                # print("left_child_data=", left_child_data, "left_children_postorder=", left_children_postorder)
                # print("left_child_data=", left_child_data, "left_children_preorder=", left_children_preorder)
                root.left = self.construct_BTree(left_children_preorder, left_children_postorder)
            else:
                root.left = None

            if len(postorder) - 1 != 0 and len(postorder) != 0:
                right_child_data = postorder[-2]
                right_children_preorder = self.get_right_children_in_preorder(right_child_data, preorder )
                right_children_postorder = self.get_right_children_in_postorder(right_child_data, preorder,postorder)
                # print("right_child_data=", right_child_data, "right_children_postorder=", right_children_postorder)
                # print("right_child_data=", right_child_data, "right_children_preorder=", right_children_preorder)
                root.right = self.construct_BTree(right_children_preorder, right_children_postorder)
            else:
                root.right = None
            return root


    def print_BTree(self, root):
        if root != None:
            print(root.data)
            self.print_BTree(root.left)
            self.print_BTree(root.right)

preorder = [8, 3, 1, 6, 4, 7, 15, 9, 20, 16]
postorder = [1, 4, 7, 6, 3, 9, 16, 20, 15, 8]

bTree = BTree()
root = bTree.construct_BTree(preorder, postorder)
bTree.print_BTree(root)
