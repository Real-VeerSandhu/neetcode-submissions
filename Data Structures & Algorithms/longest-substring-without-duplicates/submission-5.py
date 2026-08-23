class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        l = 0
        res = 0


        for i, char in enumerate(s):
            while char in window:
                window.remove(s[l])
                l += 1
            window.add(char)
            res = max(res, len(window))
        
        return res