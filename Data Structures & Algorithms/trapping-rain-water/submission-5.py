class Solution:
    def trap(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        left_max = heights[l]
        right_max = heights[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, heights[l])
                res += left_max - heights[l]
            else:
                r -= 1
                right_max = max(right_max, heights[r])
                res += right_max - heights[r]
        return res
