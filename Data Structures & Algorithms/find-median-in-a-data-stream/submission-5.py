class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if self.right and num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, num * -1)
        
        if len(self.left) > len(self.right) + 1:
            old = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, old)
        elif len(self.right) > len(self.left) + 1:
            old = heapq.heappop(self.right)
            heapq.heappush(self.left, old * -1)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0] * -1
        if len(self.left) < len(self.right):
            return self.right[0]
        return float((self.left[0]*-1 + self.right[0]) / 2.0)
        