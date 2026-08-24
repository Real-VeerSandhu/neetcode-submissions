class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])

        res = 0

        if len(intervals) <= 1:
            return 0
        
        prev_start, prev_end = intervals[0]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]

            if prev_end > cur_start:
                res += 1
                prev_end = min(prev_end, cur_end)
            else:
                prev_end = cur_end
        
        return res