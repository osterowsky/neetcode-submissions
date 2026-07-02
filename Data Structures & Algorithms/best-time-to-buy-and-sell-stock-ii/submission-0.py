class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev, profit = prices[0], 0

        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prev)
            prev = prices[i]
        
        return profit