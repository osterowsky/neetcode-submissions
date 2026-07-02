class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(sol: List[int], pick: List[bool]):
            nonlocal res

            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    sol.append(nums[i])
                    pick[i] = True
                    backtrack(sol, pick)
                    sol.pop()
                    pick[i] = False


        backtrack([], [False] * len(nums))
        return res