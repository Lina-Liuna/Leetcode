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

import llist
from llist import sllist, sllistnode

myImmutableList = sllist([1, 2, 3, 4, 5, 6])

def reverseImmutableList(mylistNode):
    if mylistNode == None:
        return
    if mylistNode!= None and mylistNode.next == None:
        print('last value of the list')
        print(mylistNode.value)
    else:
        reverseImmutableList(mylistNode.next)
        print(mylistNode.value)

reverseImmutableList(myImmutableList.first)

myImmutableList = sllist([-1, 2, 3, -4, 5, -6])

reverseImmutableList(myImmutableList.first)
