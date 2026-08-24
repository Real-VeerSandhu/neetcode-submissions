class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for stone in stones:
            maxheap.append(-stone)
        
        heapq.heapify(maxheap)

        while maxheap:
            if len(maxheap) == 1:
                return -maxheap[0]
            
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)

            if x < y:
                heapq.heappush(maxheap, -(y - x))

        return 0
            
            