class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)        
        prefixLeft = [0] * n
        prefixLeft[0] = 1
        # [1, 2, 3]
        for i in range(1, n):
            prefixLeft[i] = prefixLeft[i - 1] * nums[i - 1]
        
        prefixRight = [0] * n
        prefixRight[n - 1] = 1
        for i in range(n - 2, -1, -1):
            prefixRight[i] = prefixRight[i + 1] * nums[i + 1]
        
        res = [0] * n
        for i in range(n):
            res[i] = prefixLeft[i] * prefixRight[i]
        
        return res