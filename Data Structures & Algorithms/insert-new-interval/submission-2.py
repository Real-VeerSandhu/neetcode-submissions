class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        res = []

        new_start = newInterval[0]
        new_end = newInterval[1]

        for i in range(len(intervals)):
            if intervals[i][0] > new_end:
                # reached an interval that starts after new one ends, so everything after IS valid

                res.append([new_start, new_end])
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                return res
            elif intervals[i][1] < new_start:
                # intervals[i] ends before new start, so just add
                res.append(intervals[i])
            else:
                # occurs when intervals[i].start <= newEnd AND
                # intervals[i].end >= newStart
                new_start = min(new_start, intervals[i][0])
                new_end = max(new_end, intervals[i][1])

        res.append([new_start, new_end])
        return res
            
