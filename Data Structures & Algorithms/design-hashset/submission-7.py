class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode(0) for _ in range(8**3)]
        

    def add(self, key: int) -> None:
        cur = self.hash_set[key % len(self.hash_set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.hash_set[key % len(self.hash_set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.hash_set[key % len(self.hash_set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
# ---- HASH SET DESIGN NOTES ----
#
# Structure: array of N buckets; each bucket is a linked list (separate chaining).
# Every op: hash key -> bucket via (key % N), then scan that bucket's chain.
#
# COLLISIONS: key range 0..1M >> N buckets, so many keys share a bucket.
#   Chaining handles this: colliding keys just append to the bucket's list.
#
# n = # elements stored   |   N = # buckets (we choose this)
#
# LOAD FACTOR = n / N = average elements per bucket = average chain length.
#   It's a ratio, so it can be fractional (750/1000 = 0.75).
#   "Average" only — real buckets are lumpy (some 0, some 1, some 2+).
#   = avg work per op:  contains/add/remove scan ~n/N nodes  ->  O(n/N) avg.
#     load factor 1  -> n == N, ~1 node per chain, effectively O(1)  <- target
#     sweet spot ~0.75-2 (Java resizes at 0.75). Below = wasted memory; above = long chains.
#   Worst case: all keys hit one bucket -> chain length n -> O(n).
#
# SIZING: n <= 10,000 (at most 10k calls -> at most 10k adds).
#   Want load factor ~1 -> pick N ~= n ~= 10,000.
#
# WHY PRIME N: patterned keys (10,20,30..) sharing a factor with N all clump
#   into one bucket (10,20,30 % 10 == 0). A prime shares no factor with the
#   pattern -> keys scatter evenly -> stays near n/N avg. Use e.g. 10007.
#
# TRADE-OFF (tune via N):
#   bigger N -> smaller load factor -> shorter chains (faster) but more memory
#   smaller N -> bigger load factor -> longer chains (slower) but less memory
#
# COMPLEXITY: avg O(1) per op with good load factor + prime N; worst case O(n).

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)