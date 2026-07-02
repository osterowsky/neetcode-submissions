class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Search the correct row
        l, r, row = 0, m - 1, 0
        while l <= r:
            row = l + ((r - l) // 2)

            if matrix[row][0] <= target and matrix[row][n - 1] >= target:
                break
            elif matrix[row][0] >= target:
                r = row - 1
            else:
                l = row + 1
        
        l, r, col = 0, n - 1, 0
        while l <= r:
            col = l + ((r - l) // 2)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = col - 1
            else:
                l = col + 1
        
        return False