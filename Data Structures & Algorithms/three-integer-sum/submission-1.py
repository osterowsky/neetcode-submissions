class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        seen = defaultdict(int)

        for i, num in enumerate(nums):
            seen[num] = i
        
        for i in range(len(nums) - 1):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                diff = 0 - num1 - num2
                if diff in seen and seen[diff] not in [i, j] and sorted([diff, num1, num2]) not in triplets:
                    triplets.append(sorted([diff, num1, num2]))
        
        return triplets