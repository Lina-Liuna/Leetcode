# You are given a 2D integer array descriptions where descriptions[i] = [parent, child, isleft]
# indicates that parent is the parent of child, in a binary tree of unique values.
# if isLeft == 1, then child is the left child of parent
# if isLeft == 0, then child is the right child of parent

# Construct the binary tree described by descriptions and return its root.
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
