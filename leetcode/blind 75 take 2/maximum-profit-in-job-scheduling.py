from sys import maxsize
from heapq import heappop, heappush
from typing import List


class Solution:
    def jobSchedulingTopDownDP(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def getNext(time, jobs):
            l, r = 0, len(jobs) - 1
            nxt = len(jobs)
            while l < r:
                m = (l + r) // 2
                if jobs[m][0] < time:
                    l = m + 1
                else:
                    nxt = m
                    r = m - 1
            return nxt

        def getMaxProfit(jobs):
            if not jobs:
                return 0
            end = jobs[0][1]
            if end in dp:
                return dp[end]
            nxt = getNext(end, jobs)
            dp[end] = max(getMaxProfit(jobs[1:]), getMaxProfit(jobs[nxt:]) + jobs[0][-1])

            return dp[end]

        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        dp = {}
        return getMaxProfit(jobs)

    def jobSchedulingT2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        jobs.append((maxsize, 0, 0))

        maxProfit, h = 0, []
        for s, e, p in jobs:
            while h and h[0][0] <= s:
                maxProfit = max(maxProfit, heappop(h)[1])

            heappush(h, (e, maxProfit + p))

        return maxProfit

    def jobScheduling7(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))

        endIndex = {e: i for i, e in enumerate(endTime)}

        startTime.sort()
        endTime.sort()
        dp = {s: 0 for s in startTime}
        j = 0
        for s in startTime:
            j = 0
            while endTime[j] <= s:
                e = endTime[j]
                ps = jobs[endIndex[e]][0]
                dp[s] = max(dp[s], dp[ps] + profit[endIndex[e]])
                j += 1

        maxProfit = dp[startTime[-1]]
        while j < len(endTime):
            e = endTime[j]
            ps = jobs[endIndex[e]][0]
            dp[e] = dp[ps] + profit[endIndex[e]]
            maxProfit = max(maxProfit, dp[e])
            j += 1
        return maxProfit

    def jobScheduling8(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit))) + [(maxsize, 0, 0)]

        max_profit, h = 0, []
        for start, end, prof in jobs:
            while h and h[0][0] <= start:
                max_profit = max(max_profit, heappop(h)[1])
            heappush(h, (end, max_profit + prof))

        return max_profit


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]

startTime = [4, 2, 4, 8, 2]
endTime = [5, 5, 5, 10, 8]
profit = [1, 2, 8, 10, 4]
test = Solution()
# print(test.jobScheduling(startTime, endTime, profit))
# print(test.jobSchedulingTopDownDP(startTime, endTime, profit))
print(test.jobScheduling8(startTime, endTime, profit))
# print(test.jobScheduling7(startTime, endTime, profit))
