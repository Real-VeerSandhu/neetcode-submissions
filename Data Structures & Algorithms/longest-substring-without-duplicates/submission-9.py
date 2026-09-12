class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        window = set()

        l = 0
        res = 0

        for r, char in enumerate(s):
            while char in window:
                window.remove(s[l])
                l += 1
            window.add(char)
            res = max(res, r - l + 1)

        return res