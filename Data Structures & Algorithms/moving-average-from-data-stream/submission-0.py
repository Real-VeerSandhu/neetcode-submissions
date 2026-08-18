class MovingAverage:

    def __init__(self, size: int):
        self.n = size
        self.window_len = 0
        self.running_sum = 0
        
        self.q = collections.deque()

    def next(self, val: int) -> float:
        self.window_len += 1

        if self.window_len > self.n:
            oldest = self.q.popleft()
            self.running_sum -= oldest
            self.window_len -= 1

        self.running_sum += val
        self.q.append(val)
        
        return self.running_sum / self.window_len


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
