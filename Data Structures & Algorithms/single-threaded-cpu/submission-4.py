class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        available = []
        pending = []

        for i, (enq, proc) in enumerate(tasks):
            heapq.heappush(pending, (enq, proc, i))

        t = 0
        res = []

        while available or pending:
            while pending and pending[0][0] <= t:
                enq, proc, i = heapq.heappop(pending)
                heapq.heappush(available, (proc, i))
            
            if not available:
                t = pending[0][0]
                continue
            
            proc, i = heapq.heappop(available)
            t += proc
            res.append(i)
        
        return res