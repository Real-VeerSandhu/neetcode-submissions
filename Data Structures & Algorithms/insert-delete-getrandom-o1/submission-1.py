class RandomizedSet:

    def __init__(self):
        self.val_map = {}
        self.index_map = {}
        self.map_size = 0

    def insert(self, val: int) -> bool:
        if val in self.val_map:
            return True
        else:
            self.index_map[self.map_size] = val
            self.val_map[val] = self.map_size
            self.map_size += 1

    def remove(self, val: int) -> bool:
        if val not in self.val_map:
            return False
        else:
            old_index = self.val_map[val]
            
            end_index = self.map_size - 1
            end_val = self.index_map[end_index]

            self.val_map[end_val] = old_index
            self.index_map[old_index] = end_val

            del self.index_map[end_index]
            del self.val_map[val]
            self.map_size -= 1
            
            

    def getRandom(self) -> int:
        idx = random.randint(0, self.map_size - 1)
        return self.index_map[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()