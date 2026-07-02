class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx: int, sol: List[int]):
            if idx == len(nums):
                res.append(sol[:])
                return
            
            # Go the the left, exclude element
            backtrack(idx + 1, sol)

            # Pick element
            sol.append(nums[idx])
            backtrack(idx + 1, sol)
            sol.pop()
        
        backtrack(0, [])
        return res