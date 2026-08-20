class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        valcount = 1 + (self.count[val] if val in self.count else 0)
        # valcount = 1 + self.count.get(val, 0)
        self.count[val] = valcount

        if valcount > self.max_count:
            self.max_count = valcount
            self.stacks[valcount] = []
        
        self.stacks[valcount].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_count].pop()
        self.count[res] -= 1

        if not self.stacks[self.max_count]:
            self.max_count -= 1
        
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()