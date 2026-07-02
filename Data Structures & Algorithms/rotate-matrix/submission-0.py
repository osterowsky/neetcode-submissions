class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse the rows
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l, r = l + 1, r - 1