class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        intervals.sort(key = lambda x : x[0])
        minheap = [] # (interval_size, interval_end)
        res = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1
            
            while minheap and minheap[0][1] < q:
                # pop invalid intervals from minheap !
                heapq.heappop(minheap)
            
            res[q] = minheap[0][0] if minheap else -1
        
        final_res = []
        for q in queries:
            final_res.append(res[q])
        return final_res
            
