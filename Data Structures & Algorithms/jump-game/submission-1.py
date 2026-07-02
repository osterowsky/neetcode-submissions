class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        max_jumps, cur_idx = nums[0], 0

        while max_jumps > 0:
            cur_idx, max_jumps = cur_idx + 1, max_jumps - 1
            
            if cur_idx >= len(nums) - 1:
                return True
            
            max_jumps = max(max_jumps, nums[cur_idx])
        
        return False