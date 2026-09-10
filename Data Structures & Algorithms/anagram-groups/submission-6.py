class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            word_key = [0] * 26

            for char in word:
                word_key[ord(char) - ord('a')] += 1
            
            anagrams[tuple(word_key)].append(word)
        
        return list(anagrams.values())