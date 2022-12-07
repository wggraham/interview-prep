from copy import copy
from typing import List
from itertools import accumulate
import random
from bisect import bisect

# class Solution:
#
#     def __init__(self, w: List[int]):
#         self.weights = w
#         self.total = sum(w)
#         self.counts = {v: v/self.total for v in w}
#
#     def pickIndex(self) -> int:
#         localCounts = copy(self.counts)
#
#         while True:
#             r = random.randrange(len(self.weights))
#             localCounts[self.weights[r]] -= 1
#             if localCounts[self.weights[r]] < 0.0:
#                 return self.weights[r]

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = list(accumulate(w))

    def pickIndex(self) -> int:
        target = self.prefix_sums[-1] * random.random()
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i

    def __bin_search(self, target):
        s, e = 0, len(self.prefix_sums) - 1
        while s < e:
            m = s + (e - s) // 2
            if self.prefix_sums[m] < target:
                s = m + 1
            else:
                e = m
        return s

    def pickIndex_binsearch(self) -> int:
        target = self.prefix_sums[-1] * random.random()
        return self.__bin_search(target)

    def pickIndex_binsearch_builtin(self) -> int:
        target = self.prefix_sums[-1] * random.random()
        return bisect(self.prefix_sums, target)
w = [1, 3]
# Your Solution object will be instantiated and called as such:
obj = Solution(w)
print(obj.pickIndex_binsearch_builtin())
print(obj.pickIndex_binsearch_builtin())
print(obj.pickIndex_binsearch_builtin())
print(obj.pickIndex_binsearch_builtin())
