class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = defaultdict(int)

        for char in s:
            s_map[char] += 1
        
        t_map = defaultdict(int)

        for char in t:
            t_map[char] += 1


        return (s_map == t_map)