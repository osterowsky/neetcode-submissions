class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        prev2, prev1 = nums[0], max(nums[:2])

        for i in range(2, len(nums)):
            prev2, prev1 = prev1, max(nums[i] + prev2, prev1)

        return prev1