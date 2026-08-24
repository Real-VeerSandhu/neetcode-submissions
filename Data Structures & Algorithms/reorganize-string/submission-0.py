class Solution:
    def reorganizeString(self, s: str) -> str:
        # rearrange the chars of s so that any two adj chars are not the SAME!!!

        """
            string has length n, what maximum num

            0 1 2 3 4
            x   x   x

            0 1 2 3 4 5 6 7 8 9
        """

        freqs = Counter(s)

        maxheap = []

        for char, freq in freqs.items():
            maxheap.append((-freq, char))
        
        heapq.heapify(maxheap)

        res = []
        prev = None

        while maxheap:
            most_freq, char = heapq.heappop(maxheap)
            res.append(char)

            most_freq += 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None

            if most_freq != 0:
                prev = (most_freq, char)
                
        
        if len(res) == len(s):
            return ''.join(res)
        return ''





