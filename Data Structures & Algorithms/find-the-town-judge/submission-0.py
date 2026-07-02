class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdegrees = {}
        indegrees = {}

        for i in range(1, n + 1):
            outdegrees[i] = 0
            indegrees[i] = 0
        
        for t in trust:
            outdegrees[t[0]] += 1
            indegrees[t[1]] += 1
        
        judge = -1
        for i in range(1, n + 1):
            if outdegrees[i] == 0 and indegrees[i] == (n - 1):
                judge = i
        
        return judge