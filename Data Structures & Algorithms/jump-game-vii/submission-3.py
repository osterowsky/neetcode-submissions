class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        n = len(s)
        cache = [False] * n
        cache[-1] = True

        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                continue
            start, end = i + minJump, min(i + maxJump + 1, n)
            for j in range(start, end):
                cache[i] = cache[j] if cache[i] is False else True
        return cache[0]