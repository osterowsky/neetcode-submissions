class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missing = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in missing:
                return [missing[diff], i]
            missing[num] = i
        
        return None