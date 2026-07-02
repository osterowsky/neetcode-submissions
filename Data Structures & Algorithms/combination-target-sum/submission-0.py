class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, current, total):
            if total == target:
                res.append(current[:])
                return

            if start >= len(nums) or total > target:
                return
            
            current.append(nums[start])
            backtrack(start, current, total + nums[start])
            current.pop()
            backtrack(start + 1, current, total)


        backtrack(0, [], 0)
        return res  