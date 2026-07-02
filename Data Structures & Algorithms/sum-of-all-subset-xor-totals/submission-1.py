class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(idx: int, sol: List[int]):
            nonlocal res

            if idx == len(nums):
                subset = 0
                for num in sol:
                    subset ^= num
                res += subset
                return
            
            # Don't pick nums[idx]
            backtrack(idx + 1, sol)

            # Pick nums[idx]
            sol.append(nums[idx])
            backtrack(idx + 1, sol)
            sol.pop()
        
        backtrack(0, [])
        return res