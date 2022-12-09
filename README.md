# Leetcode

### 1. 1119 remove vowels from a string
Given a string s, remove the vowels 'a', 'e', 'i', 'o', 'u' from it, and return the new string.

### 2. 1165 single row keyboard
You have given a string keyboard of length 26 indicating the layout of the keyboard(index from 0 to 25)
initialy your finger is at index 0.
To type a character, you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|
You want to type a string word.
Write a program to calculate how much time it takes to type it with one finger.


### 3. 1265 print imutable linked list in reverse
#You are given an immutable linked list, print out all values of each node in reverse with
#the help of the following interface:
#ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
#You need to use the following functions to access the linked list(you can't access the immutableListNode directly):
#ImmutableListNode.printValue():Print value of the current node.
#ImmutableLIstNode.getNext():Return the next node.
#The input is only given to initialize the linked list internally. You must solve this problem without modifying
#the linked list. In other words, you must operate the linked list using only the mentioned APIs.

#Follow up:
#Could you solve this problem in:
#Constant space complexity?
#Linear time complexity and less than linear space complexity?

### 4. 1302 deepest leaves sum
#Given the root of a binary tree, return the sum of values of its deepest leaves.
           1
       2       3
    4     5       6
 7                    8

#input: root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]
#Output: 15

### 5. 1431 kids with the greatest number of candies

#Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

#For each kid check if there is a way to distribute extraCandies among the kids
such that he or she can have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.


### 6. 1469 find all the lonely nodes

#In a binary tree, a lonely node is a node that is the only child of its parent node.
#The root of the tree is not lonely because it does not have a parent node.
#Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree.
#Return the list in any order.

### 7. 1476 subrectangle queries
#Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers
#in the constructor and supports two methods:
#1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
   . Update all values with newValue in the subrectangle whose upper left coordinate is (row1, col1) and
     bottom right coordinate is (row2, col2)

#2. getValue(int row, int col)
  . Returns the current value of the coordinate(row, col) from the rectangle.

#Input:
#["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
#[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
#Output
#[null,1,null,5,5,null,10,5]

### 8. 1490 clone N-ary tree
#Given a root of an N-ary tree, return a deep copy(clone) of the tree.

#Each node in the n-ary tree contains a val(int) and a list (list[node]) of its children.

#class Node {
    # public int val;
    #public List<Node> children;
#}
#Nary-Tree input serialization is represented in their level order traversal, each group of children is
#separated by the null value.

#Example:
                       1
          3            2           4
    5          6

#input: root = [1, null, 3, 2, 4, null, 5, 6]
#output: [1, null, 3, 2, 4, null, 5, 6]

#Shallow copy： a new object B is created, and the fields values of A are copied over to B。
               If the field value is a reference to an object (e.g., a memory address) it copies the reference,
               all fields of the copy B are references to the same objects as the fields of original A
              The referenced objects are thus shared, so if one of these objects is modified (from A or B),
               the change is visible in the other.

### 9. 1570 dot product two spare vectors
#Given two sparse vectors, compute their dot product.
#Implement class SparseVector:
   . SparseVector(nums) Initializes the object with the vector nums
   . dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

#A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and
#compute the dot product between two SparseVector.

#Follow up: What if only one of the vectors is sparse?

#Example 1:
   Input: nums1 = [1, 0, 0, 2, 3], nums2 = [0, 3, 0, 4, 0]
   Output: 8
#Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
#v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

### 10. 1628 design an expression tree with evaluate function
#Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents
#this expression.

#The class Node is an interface you should use to implement the binary expression tree.
#The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value
#You should not remove the Node class; however, you can modify it as you wish, and you cna define other classes
#to implement it if needed.

#Example 1:
                /
         *               7
      +      2
   3     4

#input s = ["3","4","+","2","*","7","/"]
#Output: 2

### 11. 1672 richest customer wealth
#You are given an m x n integer grid accounts where accounts[i][j] is
 the amount of money the customer has in the j
 bank. Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts.
 The richest customer is the customer that has the maximum wealth.

#Input: accounts = [[1,2,3],[3,2,1]]
#Output: 6

### 12. 1689 partitioning into mini num of decimal binary numbers
#A decimal number is called deci-binary if each of its digits is either 1 or 1 without any leading zeros.
#Given a string n that represents a positive decimal integer, return the minium number of positive
#deci-binary numbers needed so that they sum up to n.

#Input: n = "32"
#Output: 3

### 13. 1874 minimize product sum of two arrays

#Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are allowed to rearrange the
#order of the elements in nums.

#input: nums1 = [5, 3, 4, 2], nums2 = [4, 2, 2, 5]
#output: 40

 2, 3, 4, 5
 5, 4, 2, 2
 10, 12, 8, 10

#Optimized solution:
#!!!!!!!!!!!!!!!!!!but the question said only allowed modify the first array!!!!!!!!!!!
#Sort one array to be in ascending order.
 Sort the other array to be in descending order.
 The product sum from the pairs of two arrays would be the minimum.

### 14. 1920 build array from permutation
#Given a zero-based permutation nums (0- indexed)
#build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

### 15. 235 lowest common ancestor of a binary search tree
#Given a binary search tree(BST), find the lowest common ancestor(LCA) of two given nodes in the BST

#Example:

                6
         2             8
     0      4        7    9
          3    5


#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#6

### 16. 236 lowest common ancestor of a binary tree
#Given a binary tree, find the lowest common ancestor(LCA) of two given nodes in the tree.

#Example:

                   3
         5                  1
    6          2       0         8
           7       4
        9     12   11  15
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Output: 3

### 17. 535 encode and decode tiny url
#Note: This is a companion problem to the System Design problem: Design TinyURL.

#TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and
 it returns a short URL such as http://tinyurl.com/4e9iAk.
 Design a class to encode a URL and decode a tiny URL.

#There is no restriction on how your encode/decode algorithm should work.
 You just need to ensure that a URL can be encoded to a tiny URL
 and the tiny URL can be decoded to the original URL

#1.    what's the traffic volume?(length of the shorteded URL?)

#Let's assume we want to serve more than 1000 billion URLS.
#If we can use 62 characters[A-Z, a-z, 0-9] for the short URLs having lenth n, then
#we can have total 62^n URLs.
#So, we should keep our URLs as short as possible given that it should fulfill the requirement.
#To make things easier,
 we can assume the alias is something like http://tinyurl.com/<alias_hash> and
 alias_hash is a fixed length string.
#Therefore, we can first just store <ID, URL>
#When a user inputs a long URL “http://www.google.com”, the system creates
 a random 7-character string like “abcd123” as ID
 and inserts entry <“abcd123”, “http://www.google.com”> into the database.
#In the run time, when someone visits http://tinyurl.com/abcd123,
 we look up by ID “abcd123” and redirect to the corresponding URL “http://www.google.com”.

#random 7-character string may be cause collision.

#One of the most simple but also effective one, is to have a database table set up this way:

#Table Tiny_Url(
#ID : int PRIMARY_KEY AUTO_INC,
#Original_url : varchar,
#Short_url : varchar
#)

### 18. 589 N-ary tree preorder traversal
#Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
#Nary-Tree input serialization is represented in their level order traversal.
#Each group of children is separated by the null value

                1
      3         2          4
  5       6

#Input: root = [1,null,3,2,4,null,5,6]
#Output: [1,3,5,6,2,4]

### 19. 1644 lowest common ancestor of a binary tree II
#Given the root of a binary tree, return the lowest common ancestor of two given nodes, p and q.
#If either node p or q does not exist in the tree, return null.
#All values of the node in the tree are unique.

#Example 1:
                   3
         5                  1
    6          2       0         8
           7       4
        9     12   11  15
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Output: 3

### 20. 1650 lowest common ancestor of binary tree III
#Given two nodes of a binary tree p and q, return their lowest common ancestor(LCA)
#Each node will have a reference to its parent node.

#Example 1:
                   3
         5                  1
    6          2       0         8
           7       4

### 21. 442 Find All Duplicates in an Array

Given an integer array num of length n where all the integers of nums are in the range[1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an aalgorithm that runs in o(n) time and uses only constant extra space.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]





























