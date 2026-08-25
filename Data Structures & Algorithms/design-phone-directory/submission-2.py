class PhoneDirectory:

    def __init__(self, maxNumbers: int):

        self.maxnums = maxNumbers
        
        self.used_nums = set()
        self.free_nums = deque()

        for num in range(self.maxnums):
            self.free_nums.append(num)

    def get(self) -> int:
        if not self.free_nums:
            return -1
        
        new_num = self.free_nums.popleft()
        self.used_nums.add(new_num)

        return new_num

    def check(self, number: int) -> bool:
        return number not in self.used_nums

    def release(self, number: int) -> None:
        if len(self.used_nums) == 0 or number not in self.used_nums:
            return
        
        self.used_nums.remove(number)
        self.free_nums.appendleft(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
