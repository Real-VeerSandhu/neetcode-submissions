class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for node in range(1, n + 1):
            adj[node] = []
        
        for s, d, w in times:
            adj[s].append((d, w))

        minheap = [(0, k)]
        shortest = {}

        while minheap:
            w1, n1 = heapq.heappop(minheap)

            if n1 in shortest: # need check to see if it was reached by something else FASTER!
                continue
            
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, (w1 + w2, n2))
        
        res = 0
        for node in range(1, n + 1):
            if node not in shortest:
                return -1
            res = max(res, shortest[node])
        
        return res
