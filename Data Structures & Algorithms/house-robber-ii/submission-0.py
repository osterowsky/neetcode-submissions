class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for n in houses:
                prev2, prev1 = prev1, max(n + prev2, prev1)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))