from heapq import heappush, heappop
from sys import maxsize
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # return points where height changes when viewed from a distance left -> right
        # building = (left, right, height), buildings[n]

        buildings.sort(key=lambda x: (x[0], x[2], x[1]))
        res = [[buildings[0][0]]]
        reach, highest = buildings[0][1], buildings[0][2]
        for stats in buildings[1:]:
            start, end, height = stats
            if reach >= end and height <= highest:
                continue
            if start > reach:
                res[-1].append(highest)
                res.append([reach])
                highest = 0

            elif height > highest:
                res[-1].append(highest)
                highest = height
                res.append([start])

            reach = max(reach, end)
        res[-1].append(highest)
        res.append([reach, 0])
        return res

    def getSkyline2(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort()
        start, end, height = buildings[0]
        res, s = [[start]], [(end, height)]

        for stats in buildings[1:]:
            start, end, height = stats

            # if end > stack.top().end
            reach, h = s.pop()
            res[-1].append(h)
            if reach < start:
                res.append([reach, 0])
                # s.append((reach, 0))

            res += [[reach]] if h > height else [[start]]
            s.append((end, height))

        reach, h = s.pop()
        res[-1].append(h)
        return res + [reach, 0]

    def getSkyline3(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for start, end, height in buildings:
            points.append((start, height, True))
            points.append((end, height, False))
        points.sort()

        sky_line, max_height, h = [], 0, [(0, maxsize)]
        for i, height, isStart in points:
            while h[0][1] <= i:
                heappop(h)

            if isStart:
                heappush(h, (-height, i))

            roof_line = -h[0][0]
            if max_height != roof_line:
                sky_line.append([i, roof_line])
                max_height = roof_line

        return sky_line

    def getSkyline4(self, buildings: List[List[int]]) -> List[List[int]]:
        points = [(start, -height, end) for start, end, height in buildings] + [(end, 0, 0) for _, end, _ in buildings]
        points.sort()

        res, heap = [[0, 0]], [(0, maxsize)]
        for i, neg_height, end in points:
            while i >= heap[0][1]:
                heappop(heap)

            if neg_height:
                heappush(heap, (neg_height, end))

            sky_line = -heap[0][0]
            if res[-1][1] != sky_line:
                res.append([i, sky_line])
        return res[1:]

    def getSkyline5(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline, live, i, n = [], [], 0, len(buildings)
        while i < n or live:
            if not live or i < n and buildings[i][0] <= -live[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heappush(live, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -live[0][1]
                while live and -live[0][1] <= x:
                    heappop(live)

            height = len(live) and -live[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],

        return skyline

    def getSkyline6(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline, live, i, n = [], [], 0, len(buildings)

        while i < n or live:
            if not live or i < n and buildings[i][0] <= -live[0][1]:
                start = buildings[i][0]
                for i, (s, e, h) in enumerate(buildings[i:], i + 1):
                    if s != start:
                        i -= 1
                        break
                    heappush(live, (-h, -e))
            else:
                start = -live[0][1]
                while live and -live[0][1] <= start:
                    heappop(live)

            height = -live[0][0] if live else 0
            if not skyline or height != skyline[-1][1]:
                skyline += [start, height],

        return skyline

    def getSkyline7(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for start, end, height in buildings:
            points += (start, height, end),
            points += (end, 0, 0),
        points.sort(key=lambda x: (x[0], -x[1]))

        sky, h, roof, reach = [[0, 0]], [(0, maxsize)], 0, 0
        for i, height, end in points:
            while h[0][1] <= i:
                heappop(h)

            if end:
                heappush(h, (-height, end))

            highest = -h[0][0]
            if sky[-1][1] != highest:
                sky += [i, highest],

        return sky[1:]

    def getSkyline8(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for start, end, height in buildings:
            points += (start, -height, end),
            points += (end, 0, 0),
        points.sort()

        sky, h, roof, reach = [[0, 0]], [(0, maxsize)], 0, 0
        for i, neg_height, end in points:
            while h[0][1] <= i:
                heappop(h)

            if end:
                heappush(h, (neg_height, end))

            highest = -h[0][0]
            if sky[-1][1] != highest:
                sky += [i, highest],

        return sky[1:]


buildings = [[0, 2, 3], [2, 5, 3]]
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
test = Solution()
print(test.getSkyline7(buildings))
print(test.getSkyline8(buildings))
