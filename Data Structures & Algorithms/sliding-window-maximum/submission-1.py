class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            deque is monotonic decreasing, left is big, right is small
             left is always the max, and will be added to res
             we will pop from right whenver adding soemthing that v
             violated the monotonci decreasing property
        """
    
        heap = []
        output = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i >= k - 1:

                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])

        return output