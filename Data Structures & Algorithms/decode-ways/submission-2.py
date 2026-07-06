class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        first, second = 0, 1
        res = 0
        while second < len(s):
            if s[first] in "12345679":
                res += 1
                if s[first] in "12" and s[second] in "123456":
                    res += 1
            first += 1
            second += 1
        
        return res