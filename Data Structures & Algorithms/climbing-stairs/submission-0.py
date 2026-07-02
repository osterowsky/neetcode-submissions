class Solution:
    def climbStairs(self, n: int) -> int:
        ways = []
        for i in range(n + 1):
            if i <= 1:
                ways.append(1)
                continue
            ways.append(ways[i - 1] + ways[i - 2])
        
        return ways[n]
