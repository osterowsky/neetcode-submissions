class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # O(nlogn) in-place sort
        res = []
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        inserted = False

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if prev_end >= start: # overlaps
                prev_start = min(prev_start, start)
                prev_end = max(prev_end, end)
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end
                interted = True
            
        if not inserted:
            res.append([prev_start, prev_end])

        return res