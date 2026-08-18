class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            nodes = beginWord + wordList

            (endWord should be in wordList)

            need to make a graph, edge:

            w1 is connected to w2 IFF :
                w1 and w2 diff by only 1 char
                can search in O(10) cuz length of word <= 10
            make a grpah then do BFS to get shortest path, if path hits endWord, done that is shortest path
        """

        adj = {}
        adj[beginWord] = []
        
        for word in wordList:
            adj[word] = []

        for source in adj:
            for target in adj:
                if source == target:
                    continue
                diff = 0
                for i in range(len(source)):
                    diff += 1 if source[i] != target[i] else 0
                if diff == 1:
                    adj[source].append(target)
        
        print(adj)
        res = 0

        q = deque()
        q.append(beginWord)
        
        visit = set()
        visit.add(beginWord)

        while q:
            res += 1
            for _ in range(len(q)):
                source = q.popleft()

                if source == endWord:
                    return res

                for nei in adj[source]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        
        
        return 0
