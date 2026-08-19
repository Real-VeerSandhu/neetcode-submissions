class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        i = 0
        res = []

        while l < len(word1) and r < len(word2):
            if i % 2 == 0:
                res.append(word1[l])
                l += 1
                i += 1
            else:
                res.append(word2[r])
                r += 1
                i += 1
        
        while l < len(word1):
            res.append(word1[l])
            l += 1
        
        while r < len(word2):
            res.append(word2[r])
            r += 1
        
        return ''.join(res)