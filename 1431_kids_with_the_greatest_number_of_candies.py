#Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

#For each kid check if there is a way to distribute extraCandies among the kids
# such that he or she can have the greatest number of candies among them.
# Notice that multiple kids can have the greatest number of candies.

class Solutions:
    MaxCandiesFlag = []
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        for num in candies:
            if num + extraCandies >= maxCandies:
                self.MaxCandiesFlag.append('True')
            else:
                self.MaxCandiesFlag.append('False')

        return self.MaxCandiesFlag

candies = [2,3,5,1,3]
extraCandies = 3
print(Solutions.kidsWithCandies(Solutions, candies, extraCandies))



