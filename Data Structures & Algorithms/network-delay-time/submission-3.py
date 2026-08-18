class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append((v, t))
        
        minheap = [(0, k)]
        shortest = {}

        while minheap:
            w, u = heapq.heappop(minheap)

            if u in shortest:
                continue
            shortest[u] = w

            for u2, w2 in adj[u]:
                if u2 not in shortest:
                    heapq.heappush(minheap, (w2 + w, u2))
        
        res = 0
        for u in range(1, n + 1):
            if u not in shortest:
                return -1
            res = max(res, shortest[u])
        
        return res