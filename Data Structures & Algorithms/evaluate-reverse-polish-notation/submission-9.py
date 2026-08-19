class Op:
    def __init__(self, arity, fn):
        self.arity = arity
        self.fn = fn

def add(left, right):
    return left + right

def subtract(left, right):
    return left - right

def multiply(left, right):
    return left * right

def divide(left, right):
    res = left / right
    return int(res)  # int() truncates toward 0

def negate(x):
    return -x

def fma(a, b, c):
    return a * b + c  # example complex op: a*b + c

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': Op(2, add),
            '-': Op(2, subtract),
            '*': Op(2, multiply),
            '/': Op(2, divide),
            'neg': Op(1, negate),
            'fma': Op(3, fma),
        }

        stack = []
        for token in tokens:
            if token in ops:
                op = ops[token]
                if len(stack) < op.arity:
                    raise Exception(f'operator {token} needs {op.arity} operands, have {len(stack)}')

                args = []
                for _ in range(op.arity):
                    args.append(stack.pop())
                args.reverse()  # restore original operand order

                stack.append(op.fn(*args))
            else:
                val = int(token)
                if not (-2**31 <= val < 2**31):
                    raise Exception(f'{val} out of range')
                stack.append(val)

        if len(stack) != 1:
            raise Exception(f'malformed expression, stack ended at size {len(stack)}')
        return stack[0]