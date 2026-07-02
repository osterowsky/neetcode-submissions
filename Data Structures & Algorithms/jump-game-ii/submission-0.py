class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [float('inf')] * n
        cache[-1] = 0

        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                cache[i] = min(cache[i], 1 + cache[j])        
        return cache[0]
