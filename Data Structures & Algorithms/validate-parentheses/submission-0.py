class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for paren in s:
            if paren not in close_to_open:
                stack.append(paren)
                continue
            
            if not stack or close_to_open[paren] != stack[-1]:
                return False
            
            stack.pop()
        
        return not stack