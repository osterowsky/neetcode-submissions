class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n * 2

        for i, num in enumerate(nums):
            res[i], res[i + n] = num, num
        
        return res
