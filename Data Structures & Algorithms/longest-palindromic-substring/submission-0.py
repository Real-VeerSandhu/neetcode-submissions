class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd len
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > resLen:
                    resLen = (R - L + 1)
                    resIdx = L
                L -= 1
                R += 1
            
            # even len
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > resLen:
                    resLen = (R - L + 1)
                    resIdx = L
                L -= 1
                R += 1
        
        return s[resIdx : resIdx + resLen]