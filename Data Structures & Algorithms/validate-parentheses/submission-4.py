class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []

        for bracket in s:
            if bracket not in close_to_open:
                stack.append(bracket)
                continue
            
            # in variant NOW is that bracket is a closing bracket
            if stack and stack[-1] == close_to_open[bracket]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0