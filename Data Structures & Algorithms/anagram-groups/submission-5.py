class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            
            anagrams[str(key)].append(word)
        

        res = []
        for a in anagrams:
            res.append(anagrams[a])
        
        return res

