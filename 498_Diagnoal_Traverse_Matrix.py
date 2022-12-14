# Given an m * n matrix mat, return an array of all the elements of the array in a diagonal order.

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

class Matrix:
    DT_Arr = []
    def Diagnoal_Traverse(self, arr, m, n):
        for line in range(0, m):
            line_arr = []
            if line % 2 == 0:
                for i in reversed(range(0, line + 1 )):
                    self.DT_Arr.append(arr[i][line - i])
            else:
                for i in range(0, line + 1):
                    self.DT_Arr.append(arr[i][line - i])
# To be Continued...
#        for line in range(1, n):

m = Matrix()
mat = [[1,2,3],[4,5,6],[7,8,9]]
m.Diagnoal_Traverse(mat, 3, 3)
print(m.DT_Arr)