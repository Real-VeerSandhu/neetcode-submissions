class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for paren in s:
            if paren in close_to_open:
                if stack and stack[-1] == close_to_open[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)
        
        return not stack