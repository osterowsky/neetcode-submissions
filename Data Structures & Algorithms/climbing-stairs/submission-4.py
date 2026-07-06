class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        first, second = 1, 2
        for i in range(3, n + 1):
            temp = second
            second = second + first
            first = temp

        return second