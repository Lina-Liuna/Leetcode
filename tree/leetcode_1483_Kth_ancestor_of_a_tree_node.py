# You are given a tree with n nodes from 0 to n - 1 in the form of a parent array parent where parent[i]
# is the parent of the ith node. The root of the tree is node 0. Find the kth ancestor of a given node.
# The kth ancestor of a tree node is the kth node in the path from that node to the root node.

# implement the TreeAncestor class:
# TreeAncestor(int n, int [] parent) initializes the object with the number of nodes in the tree and the parent array
# int getKthAncestor(int node, int k) return the kth ancestor of the given  node.
# if there is no such ancestor, return -1
# ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
# [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
# Output
# [null, 1, 0, -1]

# Explanation
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
# treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
# treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
# ftreeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor
