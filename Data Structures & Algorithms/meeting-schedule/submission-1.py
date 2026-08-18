"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = []
        for inter in intervals:
            heapq.heappush(arr, (inter.start, inter.end))
        
        prev_end = None
        while arr:
            start, end = heapq.heappop(arr)
            if prev_end is None:
                prev_end = end
                continue
            if prev_end > start:
                return False
            prev_end = end
        
        return True
        