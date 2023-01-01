# You are given a 2D integer array descriptions where descriptions[i] = [parent, child, isleft]
# indicates that parent is the parent of child, in a binary tree of unique values.
# if isLeft == 1, then child is the left child of parent
# if isLeft == 0, then child is the right child of parent

# Construct the binary tree described by descriptions and return its root.
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.

class Node:
    data = 0
    left = None
    right = None

    def __init__(self, val):
        self.data = val


class BTree:

    def get_root_data(self, descr):
        parent = [d[0] for d in descr]
        child = [d[1] for d in descr]
        for p in parent:
            if p not in child:
                return p

    def find_root_index(self, root_data, descr):
        parent = [d[0] for d in descr]
        for p in parent:
            if p == root_data:
                return parent.index(p)
        return len(descr)

    def construct_BTree(self, root_data, descr):
        if len(descr) != 0:
            root_index = self.find_root_index(root_data, descr)
            root = Node(root_data)

            if root_index == len(descr):
                root.left = None
            elif descr[root_index][2] == 1:
                root_left_data = descr[root_index][1]
                descr.pop(root_index)
                root.left = self.construct_BTree(root_left_data, descr)
            if root_index + 1 >= len(descr):
                root.right = None

            elif descr[root_index + 1] == root_data:
                root_right_data = descr[root_index + 1][1]
                descr.pop(root_index + 1)
                root.right = self.construct_BTree(root_right_data, descr)
            return root

    def print_btree(self, root):
        if root is not None:
            print(root.data)
            self.print_btree(root.left)
            self.print_btree(root.right)


descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
btree = BTree()
root_data = btree.get_root_data(descriptions)
root = btree.construct_BTree(root_data, descriptions)
btree.print_btree(root)
