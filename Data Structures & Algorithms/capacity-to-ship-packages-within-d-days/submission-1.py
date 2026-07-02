class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        while l <= r:
            w = l + ((r - l) // 2)
            
            d, temp = 1, w
            for weight in weights:
                if temp >= weight:
                    temp -= weight
                else:
                    d += 1
                    temp = w - weight
            
            if d <= days:
                r = w - 1
            else:
                l = w + 1

        return l