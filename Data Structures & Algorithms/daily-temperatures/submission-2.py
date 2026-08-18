class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        """
            temperatures = [30,38,30,36,35,40,28]


            [30,38,30,36,35,40,28]

            [30,38,38,38,38,40,40]
        """


        cur_max = temps[0]

        stack = []

        res = [0] * len(temps)

        for i, temp in enumerate(temps):
            if not stack:
                stack.append([i, temp])
            elif temp <= stack[-1][1]:
                stack.append([i, temp])
            else:
                while stack and temp > stack[-1][1]:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append([i, temp])
        
        return res
