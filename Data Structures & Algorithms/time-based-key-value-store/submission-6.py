class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        add to kv store
        -> (key, value) pair +
        -> add its timestamp <-
        """
        self.kv_store[key].append((timestamp, value))


    def _upper_bound(self, arr, target):
        """
        returns first value in arr[] that is > target
        """
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
        """
        look for kv store for key=key

        kv_store[key] -> can be many items here, list of things with (ts, value)

        need to return a (ts, value) PAIR in the kv_store[key] s.t. :
            ts <= timestamp -> LATEST possible timestamp
            RIGHTMOST one
        """
        if not self.kv_store[key]:
            return ''
        if timestamp < self.kv_store[key][0][0]:
            return ''
        
        cur_list = self.kv_store[key]
        i = self._upper_bound(cur_list, timestamp) - 1

        return cur_list[i][1]

"""
if we make a GET (key=k, timestamp=t)

assume k is valid:

what if t is < all entries in kv_store[k]??
"""

