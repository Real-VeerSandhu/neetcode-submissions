class Solution:
    def trap(self, heights: List[int]) -> int:
        
        if not heights:
            return 0
        
        l, r = 0, len(heights) - 1
        l_max, r_max = heights[l], heights[r]
        res = 0

        while l < r:
            if l_max <= r_max:
                l += 1
                l_max = max(l_max, heights[l]) # bound to >= 0
                res += l_max - heights[l]
            else:
                r -= 1
                r_max = max(r_max, heights[r]) # bound to >= 0
                res += r_max - heights[r]
        
        return res