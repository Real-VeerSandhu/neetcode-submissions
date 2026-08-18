class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)
        
        visit = set()
        visit.add(beginWord)
        q = deque()
        q.append(beginWord)

        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                source = q.popleft()
                
                if source == endWord:
                    return res
                
                for i in range(len(source)):
                    pattern = source[:i] + "*" + source[i+1:]
                    for nei in adj[pattern]:
                        if nei in visit:
                            continue
                        q.append(nei)
                        visit.add(nei)
        
        return 0

