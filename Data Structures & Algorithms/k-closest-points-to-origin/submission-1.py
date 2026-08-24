class Solution:
    def _dist(self, x, y):
        x1 = 0
        y1 = 0

        return ((x - x1)**2 + (y - y1)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxheap = []

        for x, y in points:
            heapq.heappush(maxheap, (-self._dist(x, y), [x, y]))

            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        res = []

        while maxheap:
            res.append(heapq.heappop(maxheap)[1])

        return res
        