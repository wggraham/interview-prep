from collections import deque
from math import sqrt, ceil
from sys import maxsize


class Solution:
    def nearestHotel(self, A, B):
        A = [[x + 1, y + 1] for x in range(len(A[0])) for y in range(len(A)) if A[y][x] == 1]
        res = [maxsize] * len(B)
        for i, coord1 in enumerate(B):
            x1, y1 = coord1
            for coord2 in A:
                x2, y2 = coord2
                res[i] = min(res[i], abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
        return [ceil(sqrt(x)) for x in res]

    def nearestHotel2(self, grid, coords):
        n, m, q, seen = len(grid), len(grid[0]), deque(), set()
        for i in range(n):
            for j in range(m):
                if not grid[i][j]: continue
                q.append((i, j, 0))
                seen.add((i, j))

        while q:
            i, j, dist = q.popleft()
            grid[i][j] = dist
            for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= y < n and 0 <= x < m) or (y, x) in seen: continue
                seen.add((y, x))
                q.append((y, x, dist + 1))

        return [grid[y - 1][x - 1] for y, x in coords]

    def nearestHotel3(self, grid, coords):
        q = deque([(i, j) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j]])
        while q:
            i, j = q.popleft()
            for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= y < len(grid) and 0 <= x < len(grid[0])) or grid[y][x]: continue
                grid[y][x] = grid[i][j] + 1
                q.append((y, x))

        return [grid[y - 1][x - 1] - 1 for y, x in coords]

    # fastest
    def nearestHotel4(self, grid, coords):
        n, m, q = len(grid), len(grid[0]), deque()
        for i in range(n):
            for j in range(m):
                if not grid[i][j]: continue
                q.append((i, j))

        while q:
            i, j = q.popleft()
            for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= y < n and 0 <= x < m) or grid[y][x]: continue
                grid[y][x] = grid[i][j] + 1
                q.append((y, x))

        return [grid[y - 1][x - 1] - 1 for y, x in coords]


A = [[0, 0],
     [1, 0]]
B = [[1, 1],
     [2, 1],
     [1, 2]]
# A = [[1, 0], [0, 1]]
# B = [[1, 2],
#      [1, 3]]
test = Solution()
print(test.nearestHotel(A, B))
# print(test.nearestHotel2(A, B))
print(test.nearestHotel3(A, B))
