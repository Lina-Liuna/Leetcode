#A decimal number is called deci-binary if each of its digits is either 1 or 1 without any leading zeros.
#Given a string n that represents a positive decimal integer, return the minium number of positive
#deci-binary numbers needed so that they sum up to n.

#Input: n = "32"
#Output: 3

class MiniNumDeciBinary:
    def minPartitions(nums):
        digitnum = int(nums[0])
        for char in nums:
            if int(char) > digitnum:
                digitnum = int(char)

        return digitnum

n = "27346209830709182346"
n = "2734620"
myClass = MiniNumDeciBinary
print(myClass.minPartitions(n))


