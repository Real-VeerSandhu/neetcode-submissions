class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            m = (l + r) // 2

            days_to_ship = 1
            cur = 0
            for w in weights:
                if cur + w <= m:
                    cur += w
                else:
                    days_to_ship += 1
                    cur = w

            if days_to_ship <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res