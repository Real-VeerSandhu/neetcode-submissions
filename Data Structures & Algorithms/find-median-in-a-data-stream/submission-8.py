class MedianFinder:

    def __init__(self):
        self.left = [] # maxheap
        self.right = [] # minheap

    def addNum(self, num: int) -> None:
        if self.right and num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        if len(self.left) > len(self.right) + 1:
            # move ele from left -> right
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left) + 1:
            # move ele from right -> left
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2