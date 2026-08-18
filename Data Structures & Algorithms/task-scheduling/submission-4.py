class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        # Ready to run now. Max-heap by remaining count
        ready = []
        for task, count in counts.items():
            ready.append(-1 * count)
        heapq.heapify(ready) # max heap

        # Tasks in cooldown, waiting to become ready again.
        # Each entry: (time_it_becomes_ready, remaining_count_of_task)
        waiting = deque()

        time = 0
        while ready or waiting:
            time += 1

            # Anything finished cooling down? Move it back to ready.
            if waiting and waiting[0][0] == time:
                _, new_task_cnt = waiting.popleft()
                heapq.heappush(ready, new_task_cnt)

            if ready:
                new_task_cnt = heapq.heappop(ready) + 1   # run it (one fewer use)
                if new_task_cnt < 0:                      # still has uses left
                    waiting.append((time + n + 1, new_task_cnt))
            # else: nothing ready → this tick is idle, time still advances

        return time