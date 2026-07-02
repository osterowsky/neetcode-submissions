class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid = len(nums)

        i = 0
        while i < valid:
            if nums[i] == val:
                # swap with last index
                nums[i], nums[valid - 1] = nums[valid - 1], nums[i]
                valid -= 1
            else:
                i += 1
        
        return valid
