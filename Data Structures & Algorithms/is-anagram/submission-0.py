class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)

        for char in s:
            s_freq[char] += 1
        
        t_freq = defaultdict(int)

        for char in t:
            t_freq[char] += 1
        
        return s_freq == t_freq