class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp_stack = []
        while self.stack:
            temp_stack.append(self.stack.pop())
        
        self.stack.append(x)
        while temp_stack:
            self.stack.append(temp_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


"""
queue:

10 -> 20 -> 30 ->

stack should be:

10
20
30

--- push 10

10

--- push 20


10
20



--- push 40


10
20
30

newstack:

30
20
10

push

40 30 20 10 


"""


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()