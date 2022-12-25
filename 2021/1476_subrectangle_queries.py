#Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers
#in the constructor and supports two methods:
#1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
#   . Update all values with newValue in the subrectangle whose upper left coordinate is (row1, col1) and
#     bottom right coordinate is (row2, col2)

#2. getValue(int row, int col)
#   . Returns the current value of the coordinate(row, col) from the rectangle.

#Input:
#["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
#[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
#Output
#[null,1,null,5,5,null,10,5]

class SubrectangleQueries:
    intMatrixs = [[]]
    def __init__(self, intMatrixs):
        self.intMatrixs = intMatrixs

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.intMatrixs[i][j] = newValue

    def getValue(self, row, col):
        return self.intMatrixs[row][col]

mySubrectangle = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(mySubrectangle.getValue(0,2))
mySubrectangle.updateSubrectangle(0,0,3,2,5)
print(mySubrectangle.intMatrixs)


mySubrectangle = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(mySubrectangle.getValue(0,2))
mySubrectangle.updateSubrectangle(3,0,3,2,10)
print(mySubrectangle.intMatrixs)