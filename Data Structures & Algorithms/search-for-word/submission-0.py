class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx] or
                (r, c) in visited):
                return False

            visited.add((r, c))
            result = (backtrack(r+1, c, idx+1) or
                      backtrack(r-1, c, idx+1) or
                      backtrack(r, c+1, idx+1) or
                      backtrack(r, c-1, idx+1))
            visited.remove((r, c))
            return result

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        return False