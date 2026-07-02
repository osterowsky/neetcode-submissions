class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        prefixLeft = [0] * len(nums)
        prefixLeft[0] = 1
        # [1, 2, 3]
        for i in range(1, len(nums)):
            prefixLeft[i] = prefixLeft[i - 1] * nums[i - 1]
        
        prefixRight = [0] * len(nums)
        prefixRight[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            prefixRight[i] = prefixRight[i + 1] * nums[i + 1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefixLeft[i] * prefixRight[i]
        
        return res