class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx: int, sol: List[int]):
            nonlocal res

            if idx == len(nums):
                sorted_sol = sorted(sol)
                if sorted_sol not in res:
                    res.append(sorted_sol)
                return
            
            backtrack(idx + 1, sol)

            sol.append(nums[idx])
            backtrack(idx + 1, sol)
            sol.pop()


        backtrack(0, [])
        return res