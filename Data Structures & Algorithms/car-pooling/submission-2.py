class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        (tuple) -> (start, end, numPassengers)

        if you get a start 

        """

        sorted_trips = []

        for numP, fro, to in trips:
            sorted_trips.append((fro, to, numP)) # start, end numP
        
        sorted_trips.sort()

        seats_taken = 0
        minheap = [] # (end, numP)

        for trip in sorted_trips:
            start, end, numP = trip

            while minheap and minheap[0][0] <= start:
                seats_taken -= minheap[0][1]
                heapq.heappop(minheap)

            seats_taken += numP
            if seats_taken > capacity:
                return False
            
            heapq.heappush(minheap, (end, numP))
        
        return True


