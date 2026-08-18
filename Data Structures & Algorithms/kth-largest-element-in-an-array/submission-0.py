class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for i in range(len(nums)):
            max_heap.append(nums[i] * -1)
        
        heapq.heapify(max_heap)

        while k > 0:
            if k == 1:
                return max_heap[0] * -1
            heapq.heappop(max_heap)
            k -= 1
        