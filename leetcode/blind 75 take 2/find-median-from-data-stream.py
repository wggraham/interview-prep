from heapq import heappush, heappop, heapreplace


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def __pushLeft__(self, val):
        # max of minimum values
        heappush(self.left, -val)

    def __pushRight__(self, val):
        # min of maximum values
        heappush(self.right, val)

    def addNum(self, num: int) -> None:
        self.__pushLeft__(num)
        if len(self.left) > (len(self.right) + 1):
            self.__pushRight__(-heappop(self.left))

    def findMedian(self) -> float:
        if not self.right:
            return -self.left[0]
        if len(self.left) > len(self.right):
            return self.right[0] if self.right[0] < -self.left[0] else -self.left[0]
        return (self.right[0] - self.left[0]) / 2


class MedianFinder2:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heappush(self.left, -num)
        self.__update__()

    def __update__(self):
        if len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))
        if self.right and -self.left[0] > self.right[0]:
            heappush(self.left, -heapreplace(self.right, -heappop(self.left)))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0] \
                if not self.right or self.right[0] >= -self.left[0] \
                else self.right[0]
        return (self.right[0] - self.left[0]) / 2

test = MedianFinder2()
test.addNum(1)
print(test.findMedian())
test.addNum(2)
print(test.findMedian())
test.addNum(3)
print(test.findMedian())
test.addNum(4)
print(test.findMedian())
test.addNum(5)
print(test.findMedian())
test.addNum(6)
print(test.findMedian())
test.addNum(7)
print(test.findMedian())
test.addNum(8)
print(test.findMedian())
test.addNum(9)
print(test.findMedian())
test.addNum(10)
print(test.findMedian())
