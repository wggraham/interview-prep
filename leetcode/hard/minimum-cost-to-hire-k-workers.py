from typing import List
from heapq import heappush, heapreplace, heappushpop, heappop


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        group = []
        minCost = float("inf")
        totalUnits = 0

        for cpu, units in sorted([(w / q, q) for w, q in zip(wage, quality)]):
            heappush(group, -units)
            totalUnits += units

            if len(group) == K:
                minCost = min(minCost, totalUnits * cpu)
                totalUnits += heappop(group)

        return minCost

    def mincostToHireWorkers2(self, quality: List[int], wage: List[int], K: int) -> float:
        group = []
        minCost = float("inf")
        totalUnits = 0

        for cpu, units in sorted([(w / q, q) for w, q in zip(wage, quality)]):


            if len(group) < K:
                totalUnits += units
                heappush(group, -units)
            else:
                totalUnits += heappushpop(group, -units)
                minCost = min(minCost, totalUnits * cpu)


        return minCost


quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
K = 3
test = Solution()
print(test.mincostToHireWorkers(quality, wage, K))
print(test.mincostToHireWorkers2(quality, wage, K))
