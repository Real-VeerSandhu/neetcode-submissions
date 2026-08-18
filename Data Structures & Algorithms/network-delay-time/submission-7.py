class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        min_heap = [(0, k)]

        shortest = {}

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        
        res = 0
        for i in range(1, n + 1):
            if i not in shortest:
                return -1
            res = max(res, shortest[i])
        return res