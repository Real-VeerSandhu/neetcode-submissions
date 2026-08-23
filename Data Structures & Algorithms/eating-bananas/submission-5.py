class Solution:

    def _get_eating_time(self, piles, k):
        hours = 0
        for pile in piles:
            # full_hours = pile // k
            # leftover = pile % k
            # hours += full_hours
            # if leftover > 0:
            #     hours += 1
            hours += math.ceil(pile /k)
        return hours



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        h = a limit...how much time we have to eat ALL the bananas

        """

        upper_k = max(piles) # max/worst case eating rate
        lower_k = 1

        res_rate = upper_k

        while lower_k <= upper_k:
            m = (lower_k + upper_k) // 2

            time_to_eat = self._get_eating_time(piles, m)

            if time_to_eat <= h:
                res_rate = m
                upper_k = m - 1
            else:
                lower_k = m + 1
        
        return res_rate


        
