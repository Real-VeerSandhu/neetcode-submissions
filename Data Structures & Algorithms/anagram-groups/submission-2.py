class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        ltr_map = defaultdict(list) # maps ltr freqs -> list of words


        for i, word in enumerate(strs):
            alphabet = [0] * 26 # O(26)


            # O(26)
            for char in word:
                alphabet[ord(char) - ord('a')] += 1
            
            # print(word, ':', alphabet)

            ltr_map[tuple(alphabet)].append(word)
        
        return list(ltr_map.values())

    