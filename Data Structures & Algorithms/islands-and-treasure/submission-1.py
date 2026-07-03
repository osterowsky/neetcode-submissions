from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        q = deque()
        visited = [[False] * COLS for _ in range(ROWS)]

        # Seed the queue with ALL treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited[r][c] = True

        # Single BFS pass, expanding outward from every source simultaneously
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS 
                            and not visited[nr][nc] and grid[nr][nc] != -1):
                        grid[nr][nc] = dist
                        visited[nr][nc] = True
                        q.append((nr, nc))