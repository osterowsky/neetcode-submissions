class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(sol: List[str], to_open: int, to_close: int):
            if len(sol) == 2 * n:
                res.append("".join(sol))
                return

            if to_open > 0:
                sol.append("(")
                backtrack(sol, to_open - 1, to_close + 1)
                sol.pop()

            if to_close > 0:
                sol.append(")")
                backtrack(sol, to_open, to_close - 1)
                sol.pop()

        backtrack([], n, 0)
        return res