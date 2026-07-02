class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        global_max, global_min = nums[0], nums[0]
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            global_max = max(global_max, curMax)
            global_min = min(global_min, curMin)

        return max(global_max, total - global_min) if global_max > 0 else global_max
        