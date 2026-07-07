class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        cur_start, cur_end = None, None

        for start, end in intervals:
            if cur_start is None and cur_end is None:
                cur_start, cur_end = start, end
            if start > cur_end:
                merged.append([cur_start, cur_end])
                cur_start, cur_end = start, end
            else:
                cur_start = min(cur_start, start)
                cur_end = max(cur_end, end)
        
        if cur_start is not None and cur_end is not None:
            merged.append([cur_start, cur_end])
        return merged
