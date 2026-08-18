class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # back tracking solution (brute force)
        # cant start with closed


        # can start with open

        # can only add open if close_count < open_count

        # do this recursively
        def backtrack(openN, closedN):
            if openN == closedN == n:
                # make container a string and 
                # add it to valid combs
                res.append("".join(stack)) 
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        stack = [] # current container we are making
        res = [] # list of valid combos
        
        backtrack(0,0)
        return res


        
        
        # only add open paran if open < n
        # only add close paran if closed < open
        # valid If and only if open == close == n