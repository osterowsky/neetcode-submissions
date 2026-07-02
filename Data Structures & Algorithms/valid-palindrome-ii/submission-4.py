class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def checkPalindrome(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        while l < r:
            if s[l] != s[r]:
                return checkPalindrome(s, l + 1, r) or checkPalindrome(s, l, r - 1)

            l += 1
            r -= 1

        return True