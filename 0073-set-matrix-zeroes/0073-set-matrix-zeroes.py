class Solution:
    def setZeroes(self, matrix):
        zero = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero.append((i, j))

        for i, j in zero:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
            for k in range(len(matrix)):
                matrix[k][j] = 0