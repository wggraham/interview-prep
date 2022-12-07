class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minVal = prices[0]

        for val in prices[1:]:
            profit = max(profit, val - minVal)
            minVal = min(minVal, val)
        return profit