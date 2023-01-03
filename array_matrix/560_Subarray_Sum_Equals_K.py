# Given an array of integers nums and an integer k, return the total number of sub-arrays whose sum equals to k.
# A sub-array is a contiguous non-empty sequence of elements within an array.


class sorted_array:
    sub_arr = []

    def find_sub_arr_equals_k(self, arr, k):
        i = 0
        j = len(arr) - 1
        while 0 <= i < len(arr) and 0 <= j < len(arr):
            if arr[i] + arr[j] == k:
                self.sub_arr.append((i, j))
                i = i + 1
                j = j - 1
            elif arr[i] + arr[j] > k:
                j = j - 1
            else:
                i = i + 1

    # why wrong_way_find_sub_arr_equals_k is not worked as expectly?
    # we shouldn't use for loop if we want to control the cursor by our own,
    # we must use while loop to control the cursor.
    def wrong_way_find_sub_arr_equals_k(self, arr, k):
        for i, j in zip(range(len(arr)), reversed(range(len(arr)))):
            print(i, j, arr[i], arr[j])
            if arr[i] + arr[j] == k:
                self.sub_arr.append((i, j))
            elif arr[i] + arr[j] > k:
                j = j - 1
            else:
                i = i + 1


nums = [1, 2, 3]
k = 3

sa = sorted_array()
sa.find_sub_arr_equals_k(nums, k)
print(sa.sub_arr)
print(len(sa.sub_arr))
