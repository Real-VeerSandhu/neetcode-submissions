class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)

        ready_mh = []

        for task, count in counts.items():
            ready_mh.append(-1 * count)
        heapq.heapify(ready_mh)

        time = 0
        wait_q = deque() # time, new_task_count

        while ready_mh or wait_q:
            time += 1

            if not ready_mh:
                time = wait_q[0][0]

            if wait_q and time == wait_q[0][0]:
                _, new_task_count = wait_q.popleft()
                heapq.heappush(ready_mh, new_task_count)
            
            if ready_mh:
                task_count = heapq.heappop(ready_mh) + 1
                if task_count != 0:
                    wait_q.append((time + n + 1, task_count))
        
        return time