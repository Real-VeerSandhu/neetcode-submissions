class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # needs to contain only a b c
        # no tripply a b c
        # a count is a

        maxheap = []
        
        for cnt, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(maxheap, (cnt, char))

        heapq.heapify(maxheap)

        prev = None
        res = []

        while maxheap:
            freq, char = heapq.heappop(maxheap)

            if res and len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxheap:
                    break
                freq2, char2 = heapq.heappop(maxheap)

                res.append(char2)
                freq2 += 1

                if freq2 != 0:
                    heapq.heappush(maxheap, (freq2, char2))
            else:
                res.append(char)
                freq += 1

            if freq != 0:
                heapq.heappush(maxheap, (freq, char))
        
        return ''.join(res)

            