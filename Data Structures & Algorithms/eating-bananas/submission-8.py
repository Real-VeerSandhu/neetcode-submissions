class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        h = a limit...how much time we have to eat ALL the bananas

        """

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2

            time_to_eat = 0
            for p in piles:
                hours = p // m
                left_over = p % m
                time_to_eat += hours
                if left_over:
                    time_to_eat += 1

            if time_to_eat <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
            
