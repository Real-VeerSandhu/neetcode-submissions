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
        
        d_index = self.num_map[val]

        end_index = len(self.numlist) - 1

        end_val = self.numlist[end_index]
        self.num_map[self.numlist[end_index]] = d_index

        self.numlist[end_index] = val
        self.numlist[d_index] = end_val

        del self.num_map[val]
        self.numlist.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.numlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()