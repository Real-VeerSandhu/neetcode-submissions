class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ready_pool = [] # max heap
        wait_pool = deque() # will hold (time to run, task-freq)

        task_counter = Counter(tasks)

        for task, freq in task_counter.items():
            heapq.heappush(ready_pool, -1 * freq)
        
        t = 0
        while ready_pool or wait_pool:
            t += 1

            if not ready_pool:
                t = wait_pool[0][0]

            if wait_pool and wait_pool[0][0] == t:
                _, new_freq = wait_pool.popleft()
                heapq.heappush(ready_pool, new_freq)
            
            if ready_pool:
                freq = heapq.heappop(ready_pool) + 1
                if freq != 0:
                    wait_pool.append((t + n + 1, freq))
    
        return t
