class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for right, num in enumerate(nums):
            heapq.heappush(heap, (-num, right))

            # Don't have a full window yet
            if right < k - 1:
                continue

            left = right - k + 1

            # Remove maximum candidates that are outside the window
            while heap[0][1] < left:
                heapq.heappop(heap)

            output.append(-heap[0][0])

        return output