#Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are allowed to rearrange the
#order of the elements in nums.

#input: nums1 = [5, 3, 4, 2], nums2 = [4, 2, 2, 5]
#output: 40

# 2, 3, 4, 5
# 5, 4, 2, 2
# 10, 12, 8, 10

#Optimized solution:
#!!!!!!!!!!!!!!!!!!but the question said only allowed modify the first array!!!!!!!!!!!
#Sort one array to be in ascending order.
# Sort the other array to be in descending order.
# The product sum from the pairs of two arrays would be the minimum.


#Non Optimized solution:
class minSumofTwoArrays:
    arrangedArray = []
    def rearrangeArray(self, nums, pos1, pos2):
        data = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = data
    def twoArraySum(self, nums1, nums2):
        sum = 0
        for n1, n2 in zip(nums1, nums2):
            sum = sum + n1 * n2
        return sum

    def MiniSum(self, nums1, nums2):
        data = 0
        lst = []
        for p1 in range(0, len(nums1)):
            for p2 in range(p1, len(nums1)):
                self.rearrangeArray(self, nums1, p1, p2)
                tempMiniSum = self.twoArraySum(self, nums1, nums2)
                if data > tempMiniSum or data == 0:
                    data = tempMiniSum
                    self.arrangedArray = nums1

        return data

nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]

myClass = minSumofTwoArrays

MiniSumOfTwoArray = myClass.MiniSum(myClass, nums1, nums2)
print(myClass.arrangedArray)
print(MiniSumOfTwoArray)


