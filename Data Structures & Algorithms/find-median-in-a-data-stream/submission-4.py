class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, num * -1)
        
        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, val * -1)
        elif len(self.left) > len(self.right) + 1:
            val = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, val)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0] * -1
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (self.left[0] * -1 + self.right[0]) / 2
        