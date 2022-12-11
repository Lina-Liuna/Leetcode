# Given an m * n matrix, return all elements of the matrix in spiral order
# like greedy snake.

class Matrix:

    def one_row_spiral_order(self, arr, start, end, rows_number):
        for index in range(start, end):
            print(arr[rows_number][index])

    def one_row_reverse_spiral_order(self, arr, start, end, rows_number):
        for index in range(start, end):
            print(arr[rows_number][end-start-index-1])

    def one_column_spiral_order(self, arr, start, end, column_number):
        for index in range(start, end):
            print(arr[index][column_number])

    def one_column_reverse_spiral_order(self, arr, start, end, column_number):
        for index in range(start, end):
            print(arr[end-start-index+1][column_number])

    def two_rows_or_column_spiral_order(self, arr, start_row, start_column, end_row, end_column, m, n):
        print(arr[start_row][start_column])
        if m >= n:
            self.one_column_spiral_order(arr, start_row, end_row, start_column + 1)
            self.one_column_reverse_spiral_order(arr, start_row + 1, end_row, start_column)
        else:
            self.one_row_spiral_order(arr, start_column + 1, end_column, start_row)
            self.one_row_reverse_spiral_order( arr, start_column, end_column, start_row + 1)

    def two_rows_or_column_reverse_spiral_order(self, arr, start_row, start_column, end_row, end_column, m, n):
        print(arr[end_row - 1][end_column - 1])
        if m >= n:
            self.one_column_reverse_spiral_order(arr, start_row, end_row, start_column)
            self.one_column_spiral_order(arr, start_row, end_row, start_column + 1)
        else:
            self.one_row_reverse_spiral_order(arr, start_column, end_column - 1, start_row)
            self.one_row_spiral_order(arr, start_column, end_column, start_row + 1)

    def three_rows_or_column_spiral_order(self, arr, start_row, start_column, end_row, end_column, m, n):
        self.one_row_spiral_order(arr, start_column, end_column, start_row)
        self.one_column_spiral_order(arr, start_row + 1, end_row, end_column - 1)
        self.two_rows_or_column_reverse_spiral_order( arr, start_row + 1, start_column, end_row, end_column - 1, m-1, n-1)

    def spiral_order(self, arr, start_row, start_column, end_row, end_column, m, n):
        if min(m,n) == 3:
            return self.three_rows_or_column_spiral_order(arr, 0, 0, end_row, end_column, m, n)
        elif min(m,n) == 2:
            return self.two_rows_or_column_spiral_order(arr, 0, 0, m, n, m, n)
        elif min(m,n) == 1 & m == 1:
            return self.one_column_spiral_order(arr, 0, n, n)
        elif min(m,n) == 1 & n == 1:
            return self.one_row_spiral_order(arr, 0, m, m)
        else:
            self.one_row_spiral_order(arr, 0, n, 0)
            self.one_column_spiral_order(arr, 1, m, n)
            self.one_row_reverse_spiral_order(arr, 0, n - 1, m)
            self.one_column_reverse_spiral_order(arr, 1, m, 0)
            self.spiral_order(arr, start_row + 1, start_column + 1,end_row - 1, end_column - 1, m - 1, n - 1)





marr = [[1, 3, 5], [10, 11, 16], [23, 30, 34]]
m = Matrix()

# m.one_row_spiral_order(marr, 0, 4, 0)
# m.one_row_reverse_spiral_order(marr, 0, 4, 0)
# m.one_column_spiral_order(marr, 0, 3, 0)
# m.one_column_reverse_spiral_order(marr, 0, 3, 0)
m.spiral_order(marr, 0, 0, 3, 3, 3, 3)
