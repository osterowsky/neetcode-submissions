class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            square = l + ((r - l) // 2)
            if square * square == x:
                return square
            elif square * square < x:
                l = square + 1
            else:
                r = square - 1

        return r
