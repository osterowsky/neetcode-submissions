class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        return max(seen.items(), key=lambda x : x[1])[0]