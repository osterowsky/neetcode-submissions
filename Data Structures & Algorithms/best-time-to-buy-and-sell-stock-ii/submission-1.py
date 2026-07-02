class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0

        for i in range(1, len(prices)):
            sell = prices[i]
            profit += max(0, sell - buy)
            buy = prices[i]
        
        return profit