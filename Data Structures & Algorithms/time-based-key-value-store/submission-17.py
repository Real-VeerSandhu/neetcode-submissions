class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def _upper_bound(self, a, target):
        lo = 0
        hi = len(a)

        while lo < hi:
            m = (lo + hi) // 2
            if a[m][0] <= target:
                lo = m + 1
            else:
                hi = m
        
        return lo

    def get(self, key: str, timestamp: int) -> str:
        search_space = self.store[key]

        index = self._upper_bound(search_space, timestamp) - 1

        if index == -1:
            return ''
        return self.store[key][index][1]


