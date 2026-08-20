class Solution:
    def decodeString(self, s: str) -> str:
        """




        b
        3
        a
        2
        """
        string_stack = []
        count_stack = []

        current = ''
        number = 0

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            
            elif char == '[':
                string_stack.append(current)
                count_stack.append(number)

                current = ''
                number = 0
            elif char == ']':
                prev = string_stack.pop()
                count = count_stack.pop()

                current = prev + current * count
            else:
                current += char
        
        return current
