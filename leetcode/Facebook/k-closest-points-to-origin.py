from heapq import heapify, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [(x**2 + y**2, x, y) for x, y in points]
        heapify(h)
        return [list(heappop(h)[1:]) for _ in range(k)]

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]

points = [[1,3],[-2,2]]
points = [[1,3],[-2,2],[2,-2]]
k = 2

points = [[8,-1],[-4,10],[0,1],[7,-8],[-3,-10],[-2,-3],[0,3]]
k = 6
points = [[-2,-6],[-7,-2],[-9,6],[10,3],[-8,1],[2,8]]
k = 5
test = Solution()
print(test.kClosest(points, k))
print(test.kClosest2(points, k))
