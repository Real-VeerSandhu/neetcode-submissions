class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            res += 1
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1
        
        # now recurrence
        # all bases cases are set, all centres of palindromes are set
        # EVEN centre -> means both s[i] and s[i+1] are EQUAL
        # ODD centre -> means trivially s[i], always TRUE

        # now search for palindromes of length 3 or more
        # recurrnece;
        # dp[i][j] IS PalinDROME IF
        # s[i] == s[j] AND inner thing is palindrome, i.e. dp[i+1]dp[j-1] is palindrome

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res += 1
        
        return res