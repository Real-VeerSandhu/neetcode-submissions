class FirstUnique:
    """

    """

    def __init__(self, nums: List[int]):
        self.counter = 0
        self.q = deque()
        self.unique_nums = {}
        self.seen = set()

        for num in nums:
            self.counter += 1
            if num in self.seen:
                if num in self.unique_nums:
                    del self.unique_nums[num]
            else:
                self.seen.add(num)
                self.unique_nums[num] = self.counter
        
        # self._show_state()
    
    def _show_state(self):
        print('seen set:', self.seen)
        print('uniques:', self.unique_nums)

    def showFirstUnique(self) -> int:
        if len(self.unique_nums) == 0:
            return -1
        min_c = float('inf')
        res = -1

        for num, c in self.unique_nums.items():
            if c < min_c:
                min_c = c
                res = num
        
        return res

    def add(self, value: int) -> None:
        self.counter += 1

        if value in self.seen:
            if value in self.unique_nums:
                del self.unique_nums[value]
            
            return
        
        self.seen.add(value)
        self.unique_nums[value] = self.counter


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
