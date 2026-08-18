class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):

            # assume i is centre of odd length palindrome
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # assume i is centre of even length palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res