class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((timestamp, value))

    def _upper_bound(self, arr, target):
        lo = 0
        hi = len(arr)

        while lo < hi:
            m = (lo + hi) // 2
            if arr[m][0] <= target:
                lo = m + 1
            else:
                hi = m
        return lo

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ''

        i = self._upper_bound(self.kv_store[key], timestamp) - 1

        return self.kv_store[key][i][1] if i >= 0 else ''
        
