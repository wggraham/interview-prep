from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def inBounds(y, x):
            return 0 <= x < n and 0 <= y < n

        def explore(y, x):
            total = 1
            for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                yy, xx = y + i, x + j
                if not inBounds(yy, xx): continue
                if (yy, xx) in visited: continue
                if not grid[yy][xx]: continue
                visited.add((yy, xx))
                total += explore(yy, xx)
            return total

        def setPerimeter(y, x, total):
            grid[y][x] = (island, total)
            for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                yy, xx = y + i, x + j
                if not inBounds(yy, xx): continue
                if (yy, xx) in visited2: continue
                if not grid[yy][xx]: continue
                visited2.add((yy, xx))
                setPerimeter(yy, xx, total)

        coords, maxArea, n, visited, visited2, island = [], 0, len(grid), set(), set(), 0
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    coords.append((i, j))
                    continue
                if (i, j) not in visited:
                    island += 1
                    visited.add((i, j))
                    area = explore(i, j)
                    setPerimeter(i, j, area)
                    maxArea = max(maxArea, area)

        for i, j in coords:
            seen, area = set(), 0
            for ii, jj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                y, x = i + ii, j + jj
                if not inBounds(y, x) or isinstance(grid[y][x], int): continue
                area += grid[y][x][1] if grid[y][x][0] not in seen else 0
                seen.add(grid[y][x][0])
            maxArea = max(maxArea, area + 1)

        return maxArea


grid = [[1, 0], [0, 1]]
grid = [[1, 1], [1, 0]]
grid = [[0,0],[0,0]]
test = Solution()
print(test.largestIsland(grid))
