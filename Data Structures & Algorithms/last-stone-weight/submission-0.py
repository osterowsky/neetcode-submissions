import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            max1 = heapq.heappop(stones) 
            max2 = heapq.heappop(stones)
            if max2 > max1:
                heapq.heappush(stones, max1 - max2)
        
        stones.append(0)
        return abs(stones[0])