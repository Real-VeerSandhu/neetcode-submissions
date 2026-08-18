class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        counters = []
        for word in strs:
            if not counters:
                counters.append(Counter(word))
                res.append([word])
                print(res)
                continue
            cur = Counter(word)

            group = -1
            for i, c in enumerate(counters):
                if cur == c:
                    group = i
                    break
            if group != -1:
                # print(group, (res), counters)
                res[group].append(word)
            else:
                counters.append(cur)
                res.append([word])
        
        return res
