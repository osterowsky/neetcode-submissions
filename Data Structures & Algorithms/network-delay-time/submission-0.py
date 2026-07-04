class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman-ford as handles cycle, we are guaranteed there are no negatives cycle
        # Then Dijkstra can be more thought to speed-up
        dist = [float('inf')] * n
        dist[k - 1] = 0

        for _ in range(n - 1):
            for src, dest, weight in times:
                if dist[src - 1] + weight < dist[dest - 1]:
                    dist[dest - 1] = dist[src - 1] + weight

        return max(dist) if max(dist) != float('inf') else -1