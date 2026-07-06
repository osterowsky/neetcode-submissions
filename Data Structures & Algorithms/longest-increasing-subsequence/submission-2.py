
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0] = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            best = []
            for r in range(i):
                if nums[r] < num and len(dp[r]) > len(best):
                    best = dp[r]
            dp[i] = best + [num]

        return len(dp[n - 1])