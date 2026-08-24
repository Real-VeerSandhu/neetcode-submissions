"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            prev_start, prev_end = intervals[i - 1].start, intervals[i - 1].end
            
            cur_start, cur_end = intervals[i].start, intervals[i].end

            if prev_end <= cur_start:
                continue
            else:
                return False


        return True
