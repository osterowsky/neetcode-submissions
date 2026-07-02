class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0

        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]

            if prev[1] > cur[0]: # They do overlap, remove one with longest end_time
                res += 1
                prev = cur if cur[1] < prev[1] else prev
            else:
                prev = cur

        return res
