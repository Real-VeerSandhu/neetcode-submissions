class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # current code??

        sorted_tasks = []
        minheap = []

        for i in range(len(tasks)):
            arrival_time, proc_time = tasks[i]

            sorted_tasks.append((arrival_time, i, proc_time))
        
        sorted_tasks.sort()

        i = 0
        time = sorted_tasks[0][0]

        res = []

        while i < len(sorted_tasks) or minheap:

            while i < len(sorted_tasks) and sorted_tasks[i][0] <= time:
                arr, idx, proc = sorted_tasks[i]
                heapq.heappush(minheap, (proc, idx))
                i += 1
            
            if not minheap:
                time = sorted_tasks[i][0]
            else:
                proc_selected, idx_selected = heapq.heappop(minheap)
                res.append(idx_selected)
                time += proc_selected
            
        
        return res
        

