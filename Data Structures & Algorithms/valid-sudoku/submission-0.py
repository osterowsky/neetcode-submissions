class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_in_rows = [set() for _ in range(9)]
        seen_in_cols = [set() for _ in range(9)]

        subbox = [set() for _ in range(3)]
        for i in range(len(board)):
            if i % 3 == 0:
                subbox = [set() for _ in range(3)] # reset subboxes
            for j in range(len(board)):
                val = board[i][j]
                if val == '.':
                    continue
                elif val in seen_in_rows[i] or val in seen_in_cols[j] or val in subbox[(j // 3) % 3]:
                    return False
                seen_in_rows[i].add(val)
                seen_in_cols[j].add(val)
                subbox[(j // 3) % 3].add(val)
        
        return True