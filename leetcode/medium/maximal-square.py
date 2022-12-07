from typing import List


class Solution:

    def getMaxArea(self, row):
        s = []
        mx = 0
        for i, val in enumerate(row):
            if s and s[-1][0] > val:
                mx = max(mx, self.maxInRange(s, val, i))
            s.append((val, i))

        n = len(row)
        while s:
            v, i = s.pop()
            mx = max(mx, v * (n - i))

        return mx

    def maxInRange(self, s, v, i):
        area = 0
        while s and s[-1][0] >= v:
            x,j = s.pop()
            area = max(area, x * (i - j))
        return area

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        a = [0] * len(matrix[0])
        mx = 0
        for row in matrix:
            for i, v in enumerate(row):
                if not int(v):
                    a[i] = -1
                a[i] += 1
            mx = max(mx, self.getMaxArea(a))

        return mx


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],["1", "0", "0", "1", "0"]]
matrix = [["1","1"]]
test = Solution()
print(test.maximalSquare(matrix))
