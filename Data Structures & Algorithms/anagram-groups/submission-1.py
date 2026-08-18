class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # everything is empty list

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(word)

        groups = []
        for key in (res):
            groups.append(res[key])
        return groups