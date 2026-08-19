# queue can only do: push to BACK, peek/pop from front, size and is_empty

class Queue:
    def __init__(self):
        self.q = deque()
    
    def push(self, x: int) -> None:
        self.q.append(x)
    
    def peek(self) -> int:
        if not self.q:
            return -1
        return self.q[0]
    
    def pop(self) -> int:
        if not self.q:
            return -1
        return self.q.popleft()
    
    def size(self) -> int:
        return len(self.q)
    
    def is_empty(self) -> int:
        return self.size() == 0
    
class MyStack:

    def __init__(self):
        self.q = Queue()
        

    def push(self, x: int) -> None:
        self.q.push(x)

        for _ in range(self.q.size() - 1):
            self.q.push(self.q.pop())

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q.peek()

    def empty(self) -> bool:
        return self.q.is_empty()
"""

30
20
10


FRONT -> 10 , 20, 30 <- BACK
q:

10

--

10 -> 20

20 -> 10

--

20 -> 10 -> 30:

10 -> 30 -> 20
30 -> 20 -> 10

"""




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()