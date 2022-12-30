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

### See Lina's Awesome Clean and Clear solution in 889_construct_btree_preorder_postorder.py

### 31. 2196. Create Binary Tree From Descriptions
You are given a 2D integer array descriptions where descriptions[i] = [parent, child, isleft]
indicates that parent is the parent of child, in a binary tree of unique values.
if isLeft == 1, then child is the left child of parent
if isLeft == 0, then child is the right child of parent

Construct the binary tree described by descriptions and return its root.
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.




















