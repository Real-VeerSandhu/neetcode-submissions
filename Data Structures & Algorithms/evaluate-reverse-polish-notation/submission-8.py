class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # truncate toward 0 is basiclaly math.floor


        stack = []

        for token in tokens:
            if token == '+':
                if len(stack) < 2:
                    raise Exception(f'cannot perform operation on stack with length {len(stack)}')
                right_val = stack.pop()
                left_val = stack.pop()

                stack.append(right_val + left_val)
            
            elif token == '-':
                if len(stack) < 2:
                    raise Exception(f'cannot perform operation on stack with length {len(stack)}')
                right_val = stack.pop()
                left_val = stack.pop()

                stack.append(left_val - right_val)
            elif token == '*':
                if len(stack) < 2:
                    raise Exception(f'cannot perform operation on stack with length {len(stack)}')
                right_val = stack.pop()
                left_val = stack.pop()

                stack.append(right_val * left_val)
            
            elif token == '/':
                if len(stack) < 2:
                    raise Exception(f'cannot perform operation on stack with length {len(stack)}')
                right_val = stack.pop()
                left_val = stack.pop()

                res = left_val / right_val
                stack.append(math.floor(res) if res > 0 else math.ceil(res))
            else:
                stack.append(int(token))
        
        return stack[0]
            
            
            