class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            num = nums[i]
            target = 0 - num
            l, r = i + 1, len(nums) - 1
            while l < r:
                res = nums[l] + nums[r]
                if res == target and [num, nums[l], nums[r]] not in triplets:
                    triplets.append([num, nums[l], nums[r]])
                elif res > target:
                    r -= 1
                else:
                    l += 1
            
        return triplets

