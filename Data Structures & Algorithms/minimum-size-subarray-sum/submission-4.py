class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, cur_sum, min_len = 0, 0, 0, float('inf')

        while r < len(nums):
            cur_sum += nums[r]
            r += 1

            while cur_sum >= target:
                min_len = min(min_len, r - l)
                cur_sum -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len