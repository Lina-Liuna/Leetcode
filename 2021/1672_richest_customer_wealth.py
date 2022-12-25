#You are given an m x n integer grid accounts where accounts[i][j] is
# the amount of money the customer has in the j
# bank. Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.

#Input: accounts = [[1,2,3],[3,2,1]]
#Output: 6

class Solutions:
    def maximumWealth(self, accounts:list[list[int]]) ->int:
        return max(sum(account) for account in accounts)


accounts = [[1,5],[7,3],[3,5]]
print(Solutions.maximumWealth(Solutions, accounts))