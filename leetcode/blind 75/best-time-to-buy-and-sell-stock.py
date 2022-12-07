from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minV = prices[0]

        for p in prices[1:]:
            profit = max(profit, p - minV)
            minV = min(minV, p)

        return profit


t = [7,1,5,3,6,4]
# t = [7,6,4,3,1]

test = Solution()
print(test.maxProfit(t))
