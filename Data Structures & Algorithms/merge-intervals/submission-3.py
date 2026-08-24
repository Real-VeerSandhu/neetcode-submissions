class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        prev_start, prev_end = intervals[0]

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_start, prev_end = res[-1]

            cur_start, cur_end = intervals[i]

            if prev_end >= cur_start:
                res[-1][1] = max(res[-1][1], cur_end)
            else:
                res.append([cur_start, cur_end])
        
        return res