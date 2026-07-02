class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = {0: nums[0]}

        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > cur + nums[i]:
                cur = nums[i]
            else:
                cur += nums[i]
            best[i] = cur
        
        res = best[0]
        for i in range(1, len(nums)):
            if best[i] > res:
                res = best[i]
        
        return res