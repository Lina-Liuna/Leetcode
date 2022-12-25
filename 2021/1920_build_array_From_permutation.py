#Given a zero-based permutation nums (0- indexed)
#build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

class ArrayPermutation:
    ans = []
    def array_permutaion(self, nums):
        for index in range(0, len(nums)):
            print(index, nums[index], nums[nums[index]])
            self.ans.append(nums[nums[index]])
        print(self.ans)

cls = ArrayPermutation()
cls.array_permutaion([0,2,1,5,3,4])
