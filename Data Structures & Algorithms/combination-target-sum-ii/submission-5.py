class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(idx: int, sol: List[int], curr_sum: int):
            nonlocal res

            if curr_sum == target:
                res.append(sol[:])
                return
            elif curr_sum > target or idx == len(candidates):
                return

            for i in range(idx, len(candidates)):
                # Skip duplicates: if current == previous, skip
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                num = candidates[i]
                sol.append(num)
                backtrack(i + 1, sol, curr_sum + num)
                sol.pop()
        
        backtrack(0, [], 0)
        return res