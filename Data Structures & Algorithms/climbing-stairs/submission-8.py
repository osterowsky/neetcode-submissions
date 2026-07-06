class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def ways(n: int):
            if memo[n] != -1:
                return memo[n]
            elif n <= 2:
                return n
            
            memo[n] = ways(n - 1) + ways(n - 2)
            return memo[n]
        
        return ways(n)