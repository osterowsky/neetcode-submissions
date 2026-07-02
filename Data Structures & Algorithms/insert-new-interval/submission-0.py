class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        result = []
        inserted = False

        for i, (start, end) in enumerate(intervals):
            if new_end < start:
                result.append([new_start, new_end])
                result.extend(intervals[i:])
                inserted = True
                break
            elif new_start > end:
                result.append([start, end])
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        if not inserted:
            result.append([new_start, new_end])

        return result