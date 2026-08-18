class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def can_ship(cap):
            ships = 1
            cur = 0
            for w in weights:
                if cur + w > cap:
                    ships += 1
                    cur = 0
                cur += w
            return ships <= days
        
        res = r
        while l <= r:
            m = (l + r) // 2

            if can_ship(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res

