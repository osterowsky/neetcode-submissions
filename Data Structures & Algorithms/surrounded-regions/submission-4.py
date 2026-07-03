from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row: int, col: int):
            q = deque([(row, col)])
            zeros = [(row, col)]
            touches_border = False

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        touches_border = True
                    for direction in directions:
                        d_row, d_col = row + direction[0], col + direction[1]
                        if (0 <= d_row < rows and 0 <= d_col < cols
                                and not visited[d_row][d_col] and board[d_row][d_col] == 'O'):
                            visited[d_row][d_col] = True
                            zeros.append((d_row, d_col))
                            q.append((d_row, d_col))

            if not touches_border:
                for row, col in zeros:
                    board[row][col] = 'X'
                    
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and not visited[row][col]:
                    visited[row][col] = True
                    bfs(row, col)