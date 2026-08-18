class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)

        ready_mh = []
        for task, count in counts.items():
            ready_mh.append(count * -1)
        heapq.heapify(ready_mh)
        wait_q = collections.deque() # time, task_count

        time = 0

        while wait_q or ready_mh:
            time += 1

            if wait_q and wait_q[0][0] == time:
                _, new_task_count = wait_q.popleft()
                heapq.heappush(ready_mh, new_task_count)
            
            if ready_mh:
                new_task_count = heapq.heappop(ready_mh) + 1
                if new_task_count != 0:
                    wait_q.append((time + n + 1, new_task_count)) 
        
        return time
