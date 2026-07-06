class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        memo[0] = nums[0]

        def dfs(n: int):
            if memo[n] != -1:
                return memo[n]
            elif n == 1:
                return max(memo[n - 1], nums[n])

            memo[n] = max(dfs(n - 2) + nums[n], dfs(n - 1))
            return memo[n]
        
        return dfs(n - 1)