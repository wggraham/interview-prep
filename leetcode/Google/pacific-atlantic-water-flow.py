from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def inBounds(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(i, j, ocean):
            ocean.add((i, j))
            for r, c in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if not inBounds(r, c) or (r, c) in ocean or heights[r][c] < heights[i][j]:
                    continue
                explore(r, c, ocean)

        pac, atl, n, m = set(), set(), len(heights), len(heights[0])
        for i in range(m):
            explore(0, i, pac)
            explore(n - 1, i, atl)
        for i in range(n):
            explore(i, 0, pac)
            explore(i, m - 1, atl)

        return list(pac.intersection(atl))


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
heights = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 13],
    [43, 80, 81, 82, 83, 84, 85, 86, 87, 88, 55, 14],
    [42, 79, 108, 109, 110, 111, 112, 113, 114, 89, 56, 15],
    [41, 78, 107, 128, 129, 130, 131, 132, 115, 90, 57, 16],
    [40, 77, 106, 127, 140, 141, 142, 133, 116, 91, 58, 17],
    [39, 76, 105, 126, 139, 144, 143, 134, 117, 92, 59, 18],
    [38, 75, 104, 125, 138, 137, 136, 135, 118, 93, 60, 19],
    [37, 74, 103, 124, 123, 122, 121, 120, 119, 94, 61, 20],
    [36, 73, 102, 101, 100, 99, 98, 97, 96, 95, 62, 21],
    [35, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 22],
    [34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]
]
test = Solution()
print(test.pacificAtlantic(heights))
