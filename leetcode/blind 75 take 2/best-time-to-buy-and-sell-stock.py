from typing import List
from sys import maxsize

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, total = maxsize, 0, 0

        for v in prices:
            buy = min(buy, v)
            total = max(total, v - buy)

        return total


prices = [7,6,4,3,1]

test = Solution()
print(test.maxProfit(prices))
