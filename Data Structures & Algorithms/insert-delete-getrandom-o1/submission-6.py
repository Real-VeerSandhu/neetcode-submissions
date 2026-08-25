class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.numlist = []

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        
        self.num_map[val] = len(self.numlist)
        self.numlist.append(val)

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
        
        idx = self.num_map[val]
        last_val = self.numlist[-1]

        self.numlist[idx] = last_val
        self.numlist.pop()

        self.num_map[last_val] = idx
        del self.num_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.numlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()