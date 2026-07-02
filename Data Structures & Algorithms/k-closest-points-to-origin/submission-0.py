class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # To find proximity to orgin one need to get distance
        # Heap data structure, min-heap would be perfect to retrieve smallest elements
        # Based on the distance in k range
        distances = []

        for i in range(len(points)):
            distance = (points[i][0]**2 + points[i][1]**2)**0.5
            distances.append((distance, i))
        
        heapq.heapify(distances)
        
        k_closest = []
        while k > 0:
            _, index = heapq.heappop(distances)
            k_closest.append(points[index])
            k -= 1
        
        return k_closest