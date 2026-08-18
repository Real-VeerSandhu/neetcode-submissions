"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append([interval.start, interval.end])
        
        heapq.heapify(times)
        
        days = []

        while times:
            start, end = heapq.heappop(times)
            if not days:
                days.append(end)
                continue
            
            found = -1
            for i, day_end in enumerate(days):
                if start < day_end:
                    continue
                else:
                    found = i
                    break
            
            # print('found:', found)
            if found == -1:
                # print('new day')
                days.append(end)
            else:
                # print('add to day', found)
                days[found] = end
        
        return len(days)