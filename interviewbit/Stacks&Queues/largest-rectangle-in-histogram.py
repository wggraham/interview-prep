class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        if not A: return 0
        s, a = [], 0
        A += [0]
        for i, v in enumerate(A):
            while s and v < A[s[-1]]:
                j = s.pop()
                w = i - s[-1] - 1 if s else i
                h = A[j]
                a = max(a, h * w)
            s.append(i)
        return a

    def largestContiguousRegion(self, grid):
        if not grid: return 0
        dp = [0] * len(grid[0])
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[j] = grid[i][j] + dp[j] if grid[i][j] else 0
            area = max(area, self.largestRectangleArea(dp))
        return area


A = [2, 1, 5, 6, 2, 3]
test = Solution()
print(test.largestRectangleArea(A))

b = [[0, 1, 1, 1, 0],
     [0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1]]
print(test.largestContiguousRegion(b))
