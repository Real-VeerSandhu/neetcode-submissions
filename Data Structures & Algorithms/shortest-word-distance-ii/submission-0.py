class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_locs = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.word_locs[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        """
        w1: 1 4 9
        w2: 4
        """
        word1_pos = self.word_locs[word1]
        word2_pos = self.word_locs[word2]

        res = float('inf')

        i = 0
        j = 0

        while i < len(word1_pos) and j < len(word2_pos):
            res = min(res, abs(word1_pos[i] - word2_pos[j]))

            if word1_pos[i] < word2_pos[j]:
                i += 1
            else:
                j += 1

        return res




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
