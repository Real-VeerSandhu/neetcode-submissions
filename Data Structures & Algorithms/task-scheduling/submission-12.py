class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        """

        counts = collections.Counter(tasks)

        ready_mh = [] # max heap
        for task, freq in counts.items():
            ready_mh.append(freq * -1)
        heapq.heapify(ready_mh)

        # we will identify every task, both in ready-max-heap (ready_mh) and in wait-queue (wait_q) by its FREQ

        wait_q = deque() # (time_to_run, task_freq)
        time = 0

        while ready_mh or wait_q:
            time += 1
            
            # if not ready_mh:
            #     time = wait_q[0][0]
            if wait_q and time == wait_q[0][0]:
                _, task_freq = wait_q.popleft()
                heapq.heappush(ready_mh, task_freq)
            if ready_mh:
                task_freq = heapq.heappop(ready_mh) + 1
                if task_freq != 0:
                    wait_q.append((time + n + 1, task_freq))
            

        return time