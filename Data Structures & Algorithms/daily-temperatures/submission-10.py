class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = []


        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][1] - i)
            
            stack.append((temperatures[i], i))

        return res[::-1]


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