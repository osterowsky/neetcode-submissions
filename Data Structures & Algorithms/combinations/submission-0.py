class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(idx: int, sol: List[int]):
            if len(sol) == k:
                res.append(sol[:])
                return

            for i in range(idx, n + 1):
                sol.append(i)
                backtrack(i + 1, sol)
                sol.pop()        
        
        backtrack(1, [])
        return res