class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def lcp(self, word: str, prefix_len: str) -> int:
        node = self.root

        for i in range(min(len(word), prefix_len)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word), prefix_len)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length_index = 0
        min_length_word = float('inf')
        res = ''

        for i, word in enumerate(strs):
            if len(word) < min_length_word:
                min_length_word = len(word)
                min_length_index = i
        
        if min_length_word == 0:
            return res
        
        trie = Trie()
        trie.insert(strs[min_length_index])
        prefix_len = min_length_word

        for i in range(len(strs)):
            prefix_len = trie.lcp(strs[i], prefix_len)
        return strs[min_length_index][:prefix_len]


            
