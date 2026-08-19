class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1

            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                # need a warmer day so look fwd
                if res[j] == 0:
                    j = len(temperatures)
                    break
                j += res[j]
            
            if j < len(temperatures):
                res[i] = j - i

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