class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0 # cur ptr
        self.len = 1 # TRUE LENGTH!
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < ((self.i + 1) + 1):
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1 

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps) # out of bounds check!
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.len - 1, self.i + steps) # out of bounds check!
        return self.history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)