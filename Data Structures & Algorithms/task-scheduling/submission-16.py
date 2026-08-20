class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freqs = Counter(tasks)

        print('task freqs: ', task_freqs)

        ready_mh = []

        for task, freq in task_freqs.items():
            ready_mh.append(freq * -1)
        
        heapq.heapify(ready_mh) 

        wait_q = deque() # task freq, time_to_run
        time = 0

        while ready_mh or wait_q:



            time += 1

            if not ready_mh:
                time = wait_q[0][1] # we are just waiting so can advance it

            if wait_q and wait_q[0][1] == time:
                new_freq, _ = wait_q.popleft()
                heapq.heappush(ready_mh, new_freq)
            

            if ready_mh:
                cur_task_freq = heapq.heappop(ready_mh) + 1
                if cur_task_freq != 0:
                    wait_q.append((cur_task_freq, time + n + 1))
        
        return time