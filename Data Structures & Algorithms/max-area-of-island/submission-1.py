class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int):   
            if row == rows or col == cols or row < 0 or col < 0:
                return 0
            if grid[row][col] != 1:
                return 0

            grid[row][col] = 0 

            return 1 + (
                dfs(row - 1, col) +
                dfs(row + 1, col) +
                dfs(row, col - 1) +
                dfs(row, col + 1)
            )

        area = 0
        for row in range(rows):
            for col in range(cols):
                area = max(area, dfs(row, col))
        return area    