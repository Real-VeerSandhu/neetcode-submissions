class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26 # s1 arr
        window = [0] * 26
        for char in s1:
            need[ord(char) - ord('a')] += 1

        k = len(s1)
        for i, char in enumerate(s2):
            window[ord(char) - ord('a')] += 1
            if i >= k:
                window[ord(s2[i - k]) - ord('a')] -= 1
            if window == need:
                return True

        return False