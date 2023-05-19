from sys import maxsize
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s0, s1, s2, s3 = maxsize, 0, -maxsize, 0
        for p in prices:
            s0 = min(s0, p)
            s1 = max(s1, p - s0)
            s2 = max(s2, s1 - p)
            s3 = max(s3, s2 + p)
        return max(0, s1, s3)


prices = [3, 3, 5, 0, 0, 3, 1, 4]
prices = [1, 2, 3, 4, 5]
test = Solution()
print(test.maxProfit(prices))
