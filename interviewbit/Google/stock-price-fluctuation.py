# from collections import defaultdict
# from heapq import heappush, heappop
#
#
# class StockPrice:
#
#     def __init__(self):
#         self.price = defaultdict(int)
#         self.maxHeap = []
#         self.minHeap = []
#         self.current_price = 0
#         self.current_time = 0
#
#     def __update__(self, timestamp, price):
#         if timestamp < self.current_time:
#             return
#         self.current_time = timestamp
#         self.current_price = price
#
#     def update(self, timestamp: int, price: int) -> None:
#         heappush(self.maxHeap, (-price, timestamp))
#         heappush(self.minHeap, (price, timestamp))
#         self.price[timestamp] = price
#         self.__update__(timestamp, price)
#
#     def current(self) -> int:
#         return self.current_price
#
#     def maximum(self) -> int:
#         while -self.maxHeap[0][0] != self.price[self.maxHeap[0][1]]:
#             heappop(self.maxHeap)
#         return -self.maxHeap[0][0]
#
#     def minimum(self) -> int:
#         while self.minHeap[0][0] != self.price[self.minHeap[0][1]]:
#             heappop(self.minHeap)
#         return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

from collections import defaultdict

from sortedcontainers import SortedDict


class StockPrice:
    def __init__(self):
        self.latest_time = 0
        self.price = defaultdict(int)
        self.price_frequency = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if self.price[timestamp] == price: return
        self.latest_time = max(self.latest_time, timestamp)
        old_price = self.price[timestamp]

        self.price[timestamp] = price
        self.price_frequency[price] = 1 if price not in self.price_frequency else self.price_frequency[price] + 1

        if old_price in self.price_frequency:
            self.price_frequency[old_price] -= 1
            del self.price_frequency[old_price]

    def current(self) -> int:
        return self.price[self.latest_time]

    def maximum(self) -> int:
        return self.price_frequency.peekitem()[0]

    def minimum(self) -> int:
        return self.price_frequency.peekitem(0)[0]
