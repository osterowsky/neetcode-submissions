class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res, curr = 0, 0

        seen = set()
        def dfs(row: int, col: int):   
            nonlocal curr         
            if row == rows or col == cols or row < 0 or col < 0 or (row, col) in seen:
                return
            
            seen.add((row, col))
            if grid[row][col] == 1:
                curr += 1
            else:
                return
            
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    res = max(res, curr)
                    curr = 0
                else:
                    seen.add((i, j))
        return res    