class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.is_unique = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.q and not self.is_unique[self.q[0]]:
            self.q.popleft()

        return self.q[0] if self.q else -1


    def add(self, value: int) -> None:
        if value not in self.is_unique:
            self.is_unique[value] = True
            self.q.append(value)
        else:
            self.is_unique[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
