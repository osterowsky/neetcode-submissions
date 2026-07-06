class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * (len(cost) + 1)
        memo[0] = memo[1] = 0

        def min_cost(n: int):
            if memo[n] != -1:
                return memo[n]
            
            memo[n] = min(min_cost(n-1) + cost[n-1], min_cost(n-2) + cost[n-2])
            return memo[n]
        return min_cost(len(cost))