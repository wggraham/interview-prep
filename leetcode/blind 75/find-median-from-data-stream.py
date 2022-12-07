from heapq import *


class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return large[0]
        return (large[0] - small[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
obj.addNum(-3)
obj.addNum(-4)
obj.addNum(-5)
print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())

