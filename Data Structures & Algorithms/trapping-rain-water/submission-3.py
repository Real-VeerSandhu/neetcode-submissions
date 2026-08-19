class Solution:
    def trap(self, heights: List[int]) -> int:
        left_max = 0
        right_max = 0
        res = 0

        left_arr = [0] * len(heights)
        right_arr = [0] * len(heights)

        for i, h in enumerate(heights):
            left_arr[i] = left_max
            if h > left_max:
                left_max = h
        
        for i in range(len(heights) - 1, -1, -1):
            right_arr[i] = right_max
            if heights[i] > right_max:
                right_max = heights[i]
        
        for i in range(len(heights)):
            if i == 0:
                continue
            if i == len(heights) - 1:
                continue
            
            # print('pos i=', i)
            # print('max height to my left  :', left_arr[i])
            # print('my height.             :', heights[i])
            # print('max height to my right :', right_arr[i])
            # print('.....')

            cur_water = min(left_arr[i], right_arr[i]) - heights[i]

            res += cur_water if cur_water > 0 else 0


        return res
