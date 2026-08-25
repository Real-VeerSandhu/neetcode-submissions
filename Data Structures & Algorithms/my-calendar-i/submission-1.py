class MyCalendar:
    
    def __init__(self):
        self.cal = [] # hold tuples of (start, end) events

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.cal:
            self.cal.append((startTime, endTime))
            return True
        
        for prev_start, prev_end in sorted(self.cal):
            print('prev', prev_start, prev_end)
            if startTime > prev_end:
                continue
            if endTime <= prev_start:
                continue
            if startTime < prev_end:
                return False
        
        self.cal.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)