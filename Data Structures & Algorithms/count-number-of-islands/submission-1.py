class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        def dfs(i: int, j: int):
            nonlocal seen

            if (i, j) in seen:
                return
                
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == '0':
                return # went over the grid or hit water
            
            seen.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
                        

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in seen:
                    islands += 1
                    dfs(i, j)
                else:
                    seen.add((i, j))
        
        return islands