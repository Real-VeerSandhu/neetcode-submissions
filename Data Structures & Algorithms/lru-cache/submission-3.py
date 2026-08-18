class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict() # BACK/LAST end is MRU

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key) # move to BACK
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False) # pop the LRU -> front, so not the END/LAST, last=False
        
