class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ''

        print(self.kv_store[key])
        arr = self.kv_store[key]
        l = 0
        r = len(arr) - 1
        res = ''

        while l <= r:
            m = (l + r) // 2

            if timestamp == arr[m][1]:
                return arr[m][0]
            elif timestamp > arr[m][1]:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
