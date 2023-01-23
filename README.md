# Leetcode


### 21. 442 Find All Duplicates in an Array

Given an integer array num of length n where all the integers of nums are in the range[1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an aalgorithm that runs in o(n) time and uses only constant extra space.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]


### 22. 74 Search a 2D matrix
Write an efficient algorithm that searches for a value target in an m * N integer matrix matrix.
The matrix has the following properties:
1. integers in each row are sorted from left to right
2. the first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 
Output: true

### 23. 54 Spiral Matrix
Given an m * n matrix, return all elements of the matrix in spiral order
like greedy snake.
![This is my png](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/54_Spiral_Matrix.png)
### 24. 498. Diagonal Traverse
Given an m * n matrix mat, return an array of all the elements of the array in a diagonal order.
![Lina png](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/498.%20Diagonal%20Traverse.png)

### 25. 560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of sub-arrays whose sum equals to k.
A sub-array is a contiguous non-empty sequence of elements within an array.


### 26. 796. Rotate String
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For instance, if s = 'abcde', then it will be 'bcdea' after one shift.


### 27. 1008. Construct Binary Search Tree from Preorder Traversal
Given an array of integer preorder, which represents the preorder traversal of a BST(binary search tree),
construct the tree and return it's root.
![Lina png](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/1008.%20Construct%20Binary%20Search%20Tree%20from%20Preorder.png)

### 28. 105. Construct Binary Tree from preorder and inorder traversal
Given two integer arrarys preorder and inorder where preorder is preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

### 29.106. Construct Binary Tree from inorder and postorder traversal 
Given two integer inorder and postorder when inorder is the inorder traversal of a binary tree and
postorder is the postorder traversal of the same tree, construct and return the binary tree.
![Lina png](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/106.%20construct%20binary%20tree%20from%20inorder%20and%20postorder.png)

### 30. 889. Construct Binary Tree from preorder and postorder traversal
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values
postorder is the postorder traversal of the sam tree, reconstruct and return the binary tree
If there exist multiple answers, you can return any of them
![Lina png_Awesome](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/889.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Postorder.png)

![Lina png_Awesome](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/889%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Postorder_part2.png)

#### 31. 2196. Create Binary Tree From Descriptions
You are given a 2D integer array descriptions where descriptions[i] = [parent, child, isleft]
indicates that parent is the parent of child, in a binary tree of unique values.
if isLeft == 1, then child is the left child of parent
if isLeft == 0, then child is the right child of parent

Construct the binary tree described by descriptions and return its root.
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
![Lina png](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/2196%20Create%20Binary%20Tree%20From%20Descriptions.png)

#### 32. 110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced
For this problem, a height-balanced binary tree is defined as:
A binary tree in which is the left and right subtree of every node differ in height by nor more than 1

#### 33. Maximum Depth of binary tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
#Input: root = [3,9,20,null,null,15,7]
#Output: 3

#### 34. 1448. Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X are no nodes with a value
greater than X.
Return the number of good nodes in the binary tree.

#### 35. 104. maximum depth of binary tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
#Input: root = [3,9,20,null,null,15,7]
#Output: 3

#### 36. 111. minimum depth of binary tree
Given a binary tree, find its minimum depth
The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.
Done!

#### 37. 543. diameter of binary tree
Given the root of a binary tree, return the length of the diameter of the tree
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
all above problems are done!

#### 38. 1245. tree diameter
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree
The tree is given as an array of edges where edges[i] = [u, v] is bidirectional edge
between nodes u and v.
Each node has labels in the set {0, 1, ...,edges.length}
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation:
A longest path of the tree is the path 1 - 0 - 2.

Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

#### 39.  102. binary tree level order traversal
Given the root of a binary tree, return the level order traversal of its nodes' values(from left to right,
 level by level)

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

#### 40. 226. invert binary tree

Given the root of a binary tree, invert the tree, and return its root.

#Input: root = [4,2,7,1,3,6,9]
#Output: [4,7,2,9,6,3,1]

#### 41. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children



preorder = [4, 2, 1, 3, 7, 6, 9]
inorder = [1, 2, 3, 4, 6, 7, 9]

#### 42. geeksforgeeks detect cycle in undirected graph
Given an undirected graph, the task is to check if there is a cycle in the given graph
![Lina png](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/geekforgeeks_detect_cycle_undirected_graph.png)


#### 43. premium level m 261 graph valid tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges(each edge is a pair of nodes)
write a function to check whether these edges make up a valid tree.

Input:  [[0,1],[1,2],[2,3],[1,4],[4,5]]
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

#### 44. premium  medium level 545 boundary of binary tree

Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.

Boundary includes left boundary leaves, and right boundary in order without duplicate nodes.

![Lina png](https://github.com/Lina-Liuna/Leetcode/raw/main/solution_diagrams/Premium%20Level%20Medium%20545%20boundary%20of%20binary%20tree.png)

### All Above are DONE

#### 156. Binary Tree Upside Down
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the 
same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into 
left leaf nodes. Returns the new root.












