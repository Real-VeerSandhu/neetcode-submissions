class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ready_mh = []
        counter = Counter(tasks)

        for task, freq in counter.items():
            ready_mh.append(-freq)
        
        heapq.heapify(ready_mh)

        wait_q = deque() # tuple -> (-task_freq, time_it_can_run)
        
        time = 0


        while ready_mh or wait_q:
            time += 1

            # if not ready_mh:
            #     time = wait_q[0][1]

            if wait_q and time == wait_q[0][1]:
                new_task_freq, u = wait_q.popleft()
                heapq.heappush(ready_mh, new_task_freq)
            
            if ready_mh:
                task_freq = heapq.heappop(ready_mh) + 1
                if task_freq != 0:
                    wait_q.append((task_freq, time + n + 1))
        
        return time
