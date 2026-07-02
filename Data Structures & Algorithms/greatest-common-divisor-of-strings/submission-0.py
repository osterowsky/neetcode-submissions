class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcds = []

        n = len(str2)
        for i in range(n + 1, 0, -1):
            if n % i == 0:
                gcds.append(str2[:i])
        
        m = len(str1)
        for gcd in gcds:
            if gcd * (m // len(gcd)) == str1:
                return gcd
        
        return ""