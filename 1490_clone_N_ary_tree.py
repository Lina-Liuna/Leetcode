#Given a root of an N-ary tree, return a deep copy(clone) of the tree.

#Each node in the n-ary tree contains a val(int) and a list (list[node]) of its children.

#class Node {
    # public int val;
    #public List<Node> children;
#}
#Nary-Tree input serialization is represented in their level order traversal, each group of children is
#separated by the null value.

#Example:
#                       1
#          3            2           4
#    5          6

#input: root = [1, null, 3, 2, 4, null, 5, 6]
#output: [1, null, 3, 2, 4, null, 5, 6]

#Shallow copy： a new object B is created, and the fields values of A are copied over to B。
#               If the field value is a reference to an object (e.g., a memory address) it copies the reference,
#               all fields of the copy B are references to the same objects as the fields of original A
#               The referenced objects are thus shared, so if one of these objects is modified (from A or B),
#               the change is visible in the other.
#test:
root = [1, None, 3, 2, 4, None, 5, 6]
def test_shallowCopy(root):
    ShallowCopyRoot = root
    ShallowCopyRoot[0] = 9
    return root
print(test_shallowCopy(root))
#Deep Copy:     a copy of object is copied in other object.
#               It means that any changes made to a copy of object do not reflect in the original object.
#               In python, this is implemented using “deep copy()” function.


class Node:
    val = 0
    children = []
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []

    def preorder(self, root:'Node'):
        if not root:return
        print(root.val)
        for child in root.children:
            root.preorder(child)
root = [1, None, 3, 2, 4, None, 5, 6]

root = Node(1)
root.children.append((Node(3)))
root.children.append((Node(2)))
root.children.append((Node(4)))
root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))
root.preorder(root)

class Solution:
    def clonenode(self, root:'Node') ->'Node':
        if not root:return None
        newnode = Node(root.val)
        for child in root.children:
            childclonenode = self.clonenode(child)
            newnode.children.append(childclonenode)
        return newnode
    def clonetree(self, root:'Node'):
        return self.clonenode(root)


mySolution = Solution()
myclonetree = mySolution.clonetree(root)
myclonetree.preorder(myclonetree)





