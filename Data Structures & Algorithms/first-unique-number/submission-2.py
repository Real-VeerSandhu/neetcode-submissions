class FirstUnique:

    def __init__(self, nums: List[int]):
        self._q = deque()
        self._is_unique = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self._q and not self._is_unique[self._q[0]]:
            self._q.popleft()
        
        if self._q:
            return self._q[0]
        return -1

    def add(self, value: int) -> None:
        # IF VALUE IS INSIDE Q, it is ALSO in hash map!! 
        # below gaurantees this!
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._q.append(value)
        else:
            self._is_unique[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
