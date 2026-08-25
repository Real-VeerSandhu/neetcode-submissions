class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        """
        sot

        available v.s. used

        original start time

        available rooms = minheap
        used rooms = minheap
        """

        meetings.sort()
        available = [i for i in range(n)] # no need to run heapify here! already is a heap!
        used = [] # (end_time, room_number)
        count = [0] * n # count[n] = # of meetings scheduled

        for start, end in meetings:
            # finish meetings
            while used and start >= used[0][0]:
                _, room_num = heapq.heappop(used)
                heapq.heappush(available, room_num)

            # no room is available, so we need to pop from used heap then schedule!
            if not available:
                end_time, room_num = heapq.heappop(used)

                end = end_time + (end - start)
                heapq.heappush(available, room_num)
            
            room_num = heapq.heappop(available)
            heapq.heappush(used, (end, room_num))
            count[room_num] += 1



        return count.index(max(count)) # first index i with count[i] = max(count)
        


        