class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) 
        # key = key
        # value = List of tuples, each tuple = (timestamp, value)     

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
    
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
        if key not in self.store:
            return ''
        
        item_list = self.store[key] # get the list of vals that were stored @ key

        if item_list[0][0] > timestamp:
            return ''

        # question asks, return a value such that set was called in the past
        # with a time_prev <= timestamp
        # if all time stams prev are > timestamp, impossible cuz timestamp is too in the past

        # 1 2 3 4 5 6 7

        res_index = self._upper_bound(item_list, timestamp) - 1
        return self.store[key][res_index][1] if res_index >= 0 else ''
