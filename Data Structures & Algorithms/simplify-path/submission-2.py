class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ''

        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ''
            else:
                cur += c # building cur file/dir name
        
        return '/' + '/'.join(stack)