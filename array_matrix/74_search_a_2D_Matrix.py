# Write an efficient algorithm that searches for a value target in an m * N integer matrix matrix.
# The matrix has the following properties:
# 1. integers in each row are sorted from left to right
# 2. the first integer of each row is greater than the last integer of the previous row.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

class Matrix:
    def search(self, matrix, target):
        r = []
        for row in matrix:
            if row[0] <= target <= row[len(row) - 1]:
                r = row
                break
        for item in r:
            if target == item:
                return True;
        return False

marr =[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

m = Matrix()
print(m.search(marr, 3))
print(m.search(marr, 20))
print(m.search(marr, 22))