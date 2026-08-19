class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)


        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((temp, i))
            
        return res


        """
        Input: temperatures = [30,38,30,36,35,40,28]

        read->28
        stack=[]

        stack empty -> res.append(0)

        -> stack.append((28, idx=6))

        ---

        read->40
        stack = [(28, 6)] <- top

        while stack and stack[-1] < new-val-40:
            stack.pop()

        stack = []
        stack = [(40, 5)]

        ---

        read -> 35
        stack = [(40, 5)]

        while ...

        stack = [(40, 5)] <- top is at 5, 35=idx-4 -> append 1 to res

        """