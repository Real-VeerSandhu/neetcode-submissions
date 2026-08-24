class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        maxprofit = [] # projects we can afford rn
        mincapital = [] # get minheap of all projects keyed by their captial, start from lowest capital first!

        for i in range(len(profits)):
            mincapital.append((capital[i], profits[i]))
        heapq.heapify(mincapital)

        for i in range(k):
            
            while mincapital and mincapital[0][0] <= w:
                _, p = heapq.heappop(mincapital)
                heapq.heappush(maxprofit, -p)

            if not maxprofit:
                # occurs if we could NOT add anything to maxprofit
                # thus break
                break

            w += heapq.heappop(maxprofit) * -1
        

        return w
