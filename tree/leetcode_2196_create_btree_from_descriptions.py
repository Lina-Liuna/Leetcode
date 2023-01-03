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

    def get_BTree_set(self, descr):
        btree_set = {}
        for parent, child, isleft in descr:
            if parent not in btree_set:
                btree_set[parent] = [None, None]
            if isleft == 1:
                btree_set[parent][0] = child
            else:
                btree_set[parent][1] = child
        return btree_set

    def construct_BTree_broken(self, root_data, descr):
        if len(descr) != 0:
            root_index = self.find_root_index(root_data, descr)
            root = Node(root_data)
            print(root_data, root_index, len(descr), descr)

            if root_index != len(descr):
                root_data = descr[root_index][1]
                n = self.construct_BTree(root_data, descr)
                if descr[root_index][2] == 1:
                    print('left', root_data, root_index, len(descr), descr)
                    root.left = n
                if descr[root_index][2] == 0:
                    print('right', root_data, root_index, len(descr), descr)
                    root.right = n
            else:
                root.left = None
                root.right = None
            return root


    def construct_BTree(self, btree_set, root_data):
        root = None
        if root_data:
            root = Node(root_data)
            if root_data in btree_set:
                root.left = self.construct_BTree(btree_set, btree_set[root_data][0])
                root.right = self.construct_BTree(btree_set, btree_set[root_data][1])
        return root

    def print_btree(self, root):
        if root is not None:
            print(root.data)
            self.print_btree(root.left)
            self.print_btree(root.right)


descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
btree = BTree()
root_data = btree.get_root_data(descriptions)
btree_set = btree.get_BTree_set(descriptions)
root = btree.construct_BTree(btree_set, root_data)
btree.print_btree(root)


