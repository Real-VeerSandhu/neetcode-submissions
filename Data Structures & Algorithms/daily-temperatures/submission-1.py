class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            Input: temperatures = [30,38,30,36,35,40,28]

            Output: [1,4,1,2,1,0,0]

            30, 38, 30, 36, 35, 40, 28

            0. stack = [30], max = 30
            1. stack = [38]

            30, 38, 38, 38, 38, 40, 40





        """

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                p_temp, p_i = stack.pop()
                res[p_i] = i - p_i # difference between indices
            
            stack.append([temp, i])
        
        return res
    
