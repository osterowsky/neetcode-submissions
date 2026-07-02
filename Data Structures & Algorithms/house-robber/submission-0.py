class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        max_rob = [0] * len(nums)
        max_rob[0], max_rob[1] = nums[0], max(nums[:2])

        for i in range(2, len(nums)):
            cur = nums[i]
            if cur + max_rob[i - 2] > max_rob[i - 1]:
                max_rob[i] = cur + max_rob[i - 2]
            else:
                max_rob[i] = max_rob[i - 1]

        return max(max_rob)