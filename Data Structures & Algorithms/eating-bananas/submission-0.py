class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = l + ((r - l) // 2)
            hours = 0
            for num in piles:
                hours += math.ceil(num / k)
            
            if hours <= h:
                r = k - 1
            else:
                l = k + 1

        return l