class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
            Input: arr = [2,4,5,8], k = 2, x = 6

            0 1 2 3 4 5 6


        """
        

        
        l = 0
        r = len(arr) - k

        while l < r:
            m = (l + r) // 2
            left_dist = abs(x - arr[m])
            right_dist = abs(x - arr[m + k]) # new val right of end of window

            if right_dist < left_dist:
                l = m + 1
            else:
                r = m
        
        return arr[l:l+k]
                

        
        
        