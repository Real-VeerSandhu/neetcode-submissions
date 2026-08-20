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
        # s="2[a3[b]]c"


        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '[':
                count_stack.append(number)
                string_stack.append(current)

                current = ''
                number = 0
            elif char == ']':
                prev_count = count_stack.pop()
                prev_string = string_stack.pop()

                current = prev_string + prev_count * current
            else:
                current += char

        return current