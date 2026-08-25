class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.COUNT = 2
        self.vectors = [v1, v2]
        self.iters = [0, 0]
        self.zig = 0 if len(v1) != 0 else 1

    def next(self) -> int:
        
        val = self.vectors[self.zig][self.iters[self.zig]]

        self.iters[self.zig] += 1

        self.zig = (self.zig + 1) % (self.COUNT)
        if self.iters[self.zig] >= len(self.vectors[self.zig]):
            self.zig = (self.zig + 1) % (self.COUNT)

        return val
        
        

    def hasNext(self) -> bool:
        for i in range(self.COUNT):
            if self.iters[i] < len(self.vectors[i]):
                return True

        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
