class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i, t in enumerate(tasks):
            t.append(i) # preserve original index
        
        tasks.sort(key = lambda x : x[0]) # tasks contain -> [enq, proc, i]
        res = []
        minheap = []

        i = 0
        time = tasks[0][0] # smallest q time

        while i < len(tasks) or minheap:
            while i < len(tasks) and time >= tasks[i][0]: # enqueue time of task[i] has ALREADY PASSED !!!
                heapq.heappush(minheap, (tasks[i][1], tasks[i][2]))
                i += 1

            if not minheap:
                time = tasks[i][0]
            else:
                cur_proc_time, cur_idx = heapq.heappop(minheap)
                time += cur_proc_time
                res.append(cur_idx)
        
        return res

