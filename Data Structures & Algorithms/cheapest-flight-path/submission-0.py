import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Directed, cyclic, weight & positive graph
        # Let's go with dijkstra, if visited[dst] we stop
        # We also need to measure number of stops
        adj_list = [[] for _ in range(n)]
        for s, d, p in flights:
            adj_list[s].append((d, p))

        visited = [False] * n
        distance = [float('inf')] * n
        distance[src] = 0

        pq = [(0, src)]
        while pq:
            dist, idx = heapq.heappop(pq)
            if visited[idx]:
                continue

            visited[idx] = True
            if visited[dst]:
                return distance[idx]

            for d, p in adj_list[s]:
                if not visited and distance[idx] + p < distance[d]:
                    distance[d] = distance[idx] + p
                    heapq.heappush(pq, (distance[d], d))
