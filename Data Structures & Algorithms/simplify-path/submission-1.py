class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        items = path.split('/')
        # print(items)
        for cur in items:
            # print('item: ', cur,  '|')
            if cur == '..':
                if stack:
                    stack.pop()
            elif cur != '' and cur != '.':
                stack.append(cur)
            # print(stack)
            # print('\n')
        

        return '/' + '/'.join(stack)