class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(c: str) -> bool:
            l, r = 0, len(c) - 1
            while l < r:
                if c[l] != c[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(sol: List[str], rest: str):
            if len(rest) == 0:
                res.append(sol[:])
                return 
            
            interim = ""
            for i in range(len(rest)):
                interim += rest[i]
                if is_palindrome(interim):
                    sol.append(interim)
                    backtrack(sol, rest[i + 1:])
                    sol.pop()
        
        backtrack([], s)
        return res