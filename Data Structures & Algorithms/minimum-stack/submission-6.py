class MinStack:

    def __init__(self):
        self.stack = [(float('inf'), float('inf'))] # tuple -> (val, min up to val)

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        if not self.stack:
            raise Exception("stack is empty")
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise Exception("stack is empty")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            raise Exception("stack is empty")
        return self.stack[-1][1]
