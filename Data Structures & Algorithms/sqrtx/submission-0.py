class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        l, r = 1, x

        while l <= r:
            square = l + ((r - l) // 2)
            if square * square == x:
                return square
            elif square * square < x:
                l = square + 1
            else:
                r = square - 1

        return r
