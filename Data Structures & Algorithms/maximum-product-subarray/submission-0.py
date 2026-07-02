class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0]] * len(nums) # max_here, min_here
        dp[0] = [nums[0], nums[0]]
        
        cur_max = nums[0]
        for i in range(1, len(nums)):
            max_here = max(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            min_here = min(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            dp[i] = [max_here, min_here]
            cur_max = max(cur_max, max_here)
        
        return cur_max