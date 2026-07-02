class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(perm: List[int], placed: List[int]):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            prev = None
            for i in range(len(nums)):
                if not placed[i] and prev != nums[i]:
                    perm.append(nums[i])
                    placed[i] = True
                    backtrack(perm, placed)
                    perm.pop()
                    placed[i] = False
                    prev = nums[i]
                        
        backtrack([], [False] * len(nums))
        return res