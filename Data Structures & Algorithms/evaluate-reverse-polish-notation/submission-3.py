class Solution:
    def eval_operation(self, operator: str, left: int, right: int) -> int:
        left = int(left)
        right = int(right)
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            ans = left / right
            return math.floor(ans) if ans >= 0 else math.ceil(ans)
        return 0
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(self.eval_operation(token, left, right))
            else:
                stack.append(int(token))
        
        return int(stack[0])

