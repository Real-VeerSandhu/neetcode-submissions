class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        """

            Input: temperatures = [30,38,30,36,35,40,28]

            28. []. res = 0

            40. [28] -> [40]. res = 0

            35. [40] -> [40, 35]. res = 1

            36. [40, 35] -> [40, 36]

            30 [28, 35, 36] -> [28, 30]



        """

        for i, temp in enumerate(temperatures[::-1]):
            
            while stack and temp >= stack[-1][1]:
                stack.pop()
            
            if stack:
                res.append(i - stack[-1][0])
            else:
                res.append(0)
            
            stack.append((i, temp))
        
        return res[::-1]