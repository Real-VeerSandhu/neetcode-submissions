class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.index_to_val = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.val_to_index[val] = self.size + 1
        self.index_to_val[self.size + 1] = val
        self.size += 1

        """
        10, 20, 30, 40

        10 : 1
        1 : 10


        --

        10 : 1
        1 : 10
        20 : 2
        2 : 20


        """

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        end_index = self.size
        end_val = self.index_to_val[end_index]

        d_index = self.val_to_index[val]
        d_val = val

        self.index_to_val[d_index] = end_val
        self.val_to_index[d_val] = end_index

        self.val_to_index[end_val] = d_index

        del self.index_to_val[end_index]
        del self.val_to_index[d_val]

        self.size -= 1

    def getRandom(self) -> int:

        return self.index_to_val[random.randint(1, self.size)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()