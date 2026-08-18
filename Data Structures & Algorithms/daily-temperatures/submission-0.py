class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        # 30,38,30,36,35,40,28
        # 30, 38
        # res.append(1)
        # 30, 38, 30, 36, 35, 40
        # res.append(4)
        # 30, 38, 30, 36

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped_temp, popped_i = stack.pop()
                res[popped_i] = abs(i - popped_i)
            stack.append([temp, i])   
                 
        return (res)