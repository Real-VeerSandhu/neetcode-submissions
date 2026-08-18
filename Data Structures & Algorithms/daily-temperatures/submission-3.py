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
        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            cur_temp = temperatures[i]

            # if not stack:
            #     stack.append((i, cur_temp))
            #     res.append(0)
            #     continue

            # print(f"index:{i}, val:{cur_temp}")
            # print(stack)
            # print(res)
            # print('---')

            while stack and stack[-1][1] <= cur_temp:
                stack.pop()
            
            res.append(stack[-1][0] - i if stack else 0)
            stack.append((i, cur_temp))
        
        # print('final')
        # print(res)
        # print(stack)
        
        return res[::-1]
