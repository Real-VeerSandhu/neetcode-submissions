class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        - - -


          _
          

        _

        - - -
        """

        def get_area(i):
            l = i
            r = i

            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            while r < len(heights) and heights[r] >= heights[i]:
                r += 1

            # print(f"width: {(r - 1) - (l + 1) + 1}")
            # print(f"height: {heights[i]}")

            return ((r - 1) - (l + 1) + 1) * heights[i]
        

        res = 0
        for i, h in enumerate(heights):
            # print('--')
            # print('i:', i)
            res = max(res, get_area(i))
        
        return res
        
        

