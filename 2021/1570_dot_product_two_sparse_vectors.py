#Given two sparse vectors, compute their dot product.
#Implement class SparseVector:
#   . SparseVector(nums) Initializes the object with the vector nums
#   . dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

#A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and
#compute the dot product between two SparseVector.

#Follow up: What if only one of the vectors is sparse?

#Example 1:
#   Input: nums1 = [1, 0, 0, 2, 3], nums2 = [0, 3, 0, 4, 0]
#   Output: 8
#Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
#v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

class SparseVector:
    """A simple Sparse vector class"""
    nums = []
    dict = {}

    def __init__(self, nums):
        self.nums = nums

    def SparseOptimize(self):
        self.dict = {}
        for index, val in enumerate(self.nums):
            if val != 0:
                self.dict[index] = val

    def dotProduct(self, vec):
        sum = 0
        for key in self.dict:
            if key in vec.dict:
                sum = sum + self.dict[key] * vec.dict[key]
        return sum

    def dotProduct_notoptimized(self, vec):
        print(sum(x*y for x, y in zip(self.nums, vec.nums)))
        
v1 = SparseVector([1, 0, 0, 2, 3])
v2 = SparseVector([0, 3, 0, 4, 0])
v1.SparseOptimize()
v2.SparseOptimize()
print(v1.dotProduct(v2))






