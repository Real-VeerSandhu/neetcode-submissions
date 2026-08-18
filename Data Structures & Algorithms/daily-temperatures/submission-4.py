class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        temperatures = [30,38,30,36,35,40,28]

        tmp = [26, 27, 40, 28]

        stack should be increasing -> as u pop, get bigger values

        stack []


        stack = [ i-40 , i-36 ] <- top

        output = [1,4,1,2,1,0,0]
        """

        stack = [] # index, temp
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, prev_temp = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((i, temp))
        
        return res
