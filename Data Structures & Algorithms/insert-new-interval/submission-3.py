class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0]
        left = 0
        right = n - 1

        while left <= right:
            m = (left + right) // 2
            if intervals[m][0] < target:
                left = m + 1
            else:
                right = m - 1
        
        intervals.insert(left, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            
        return res