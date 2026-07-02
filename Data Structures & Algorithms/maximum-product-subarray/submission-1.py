class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max, prev_min = nums[0], nums[0]
        cur_max = prev_max

        for i in range(1, len(nums)):
            max_here = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            min_here = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            cur_max = max(cur_max, max_here)
            prev_max, prev_min = max_here, min_here
        
        return cur_max