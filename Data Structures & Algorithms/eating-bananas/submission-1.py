class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours_to_eat(speed):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / speed)
            return total_hours
        
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            m = (l + r) // 2
            hours = hours_to_eat(m)

            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res



