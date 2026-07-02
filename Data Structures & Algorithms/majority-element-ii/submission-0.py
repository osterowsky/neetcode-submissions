class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > n / 3 and num not in res:
                res.append(num)
            
        return res