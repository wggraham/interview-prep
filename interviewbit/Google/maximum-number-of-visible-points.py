from typing import List
from math import atan2, pi


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angle = pi * angle / 180
        rads = [atan2(p[1] - location[1], p[0] - location[0]) for p in points
                if not (p[0] == location[0] and p[1] == location[1])]
        originPoints = len(points) - len(rads)
        rads += [r + 2.0 * pi for r in rads if r < angle]
        rads.sort()

        j, mostPoints = 0, 0
        for i, r in enumerate(rads):
            while r - rads[j] > angle: j += 1
            mostPoints = max(mostPoints, i - j + 1)

        return mostPoints + originPoints


points = [[2, 1], [2, 2], [3, 3]]
points = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]]
angle = 0
location = [1, 1]
test = Solution()
print(test.visiblePoints(points, angle, location))
