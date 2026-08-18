class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)

        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = collections.deque() #{-cnt, idletime}

        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time