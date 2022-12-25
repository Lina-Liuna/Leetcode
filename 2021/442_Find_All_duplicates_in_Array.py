# Given an integer array num of length n where all the integers of nums are in the range[1, n]
# and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an aalgorithm that runs in o(n) time and uses only constant extra space.

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

class DuplicateArray:
    array = []
    duplicate_arr = []
    length = 0

    def find_duplicate(self, arr):
        for item in arr:
            if item not in self.array:
                self.array.append(item)
            else:
                self.duplicate_arr.append(item)

        return self.duplicate_arr


nums = [4,3,2,7,8,2,3,1]
darr = DuplicateArray()

print(darr.find_duplicate(nums))