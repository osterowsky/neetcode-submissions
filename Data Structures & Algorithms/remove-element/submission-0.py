class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid, last_idx = len(nums), len(nums) - 1

        i = 0
        while i < valid:
            if nums[i] == val:
                # swap with last index
                nums[i], nums[last_idx] = nums[last_idx], nums[i]
                valid -= 1
                last_idx -= 1
                i -= 1
            i += 1
        
        return valid
