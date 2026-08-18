class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
            Input: arr = [2,4,5,8], k = 2, x = 6


        """
        

        def lower_bound(a, target):
            # returns first a[i] >= target
            lo = 0
            hi = len(a)
            while lo < hi:
                m = (lo + hi) // 2
                if a[m] < target:
                    lo = m + 1
                else:
                    hi = m
            return lo
        
        def upper_bound(a, target):
            # returns first a[i] > target
            lo = 0
            hi = len(a)
            while lo <= hi:
                m = (lo + hi) // 2
                if a[m] < target:
                    lo = m + 1
                else:
                    hi = m
            return lo
        
        def first_equal(a, target):
            i = lower_bound(a, target)
            return i if i < len(a) and a[i] == target else -1
        
        def last_equal(a, target):
            i = upper_bound(a, target) - 1
            return i if i >= 0 and a[i] == target else -1

        def smallest_greater(a, target):
            return upper_bound(a, target)
        
        def smallest_ge(a, target):
            return lower_bound(a, target)
        
        def largest_less(a, target):
            return lower_bound(a, target) - 1
        
        def largest_le(a, target):
            return upper_bound(a, target) - 1
        
        l = 0
        r = len(arr) - k

        while l < r:
            m = (l + r) // 2
            left_dist = abs(x - arr[m])
            right_dist = abs(x - arr[m + k])
            # m = left most value of WINDOW
            # if left_dist > right_dist: # math works out here, value to right is closer
            if right_dist < left_dist:
                l = m + 1
            else:
                r = m
        
        return arr[l:l+k]
                

        
        
        