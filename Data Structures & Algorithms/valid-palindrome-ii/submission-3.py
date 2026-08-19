class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s[l + 1 : r + 1]) or is_palindrome(s[l : r])
            l += 1
            r -= 1
        
        return True
