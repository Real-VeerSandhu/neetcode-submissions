class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) + int(right))
            elif t == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) - int(right))
            elif t == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) * int(right))
            elif t == '/':
                right = stack.pop()
                left = stack.pop()
                res = int(left) / int(right)
                if res < 0:
                    res = math.floor(res * -1) * -1
                else:
                    res = math.floor(res)
                stack.append(res)
            else:
                stack.append(int(t))
        
        return stack[0]


        # -100 / 33 = -3.3333