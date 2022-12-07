class Solution:
    def black(self, grid):
        adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def inBound(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(i, j):
            if not inBound(i, j): return
            if (i, j) in seen: return
            if grid[i][j] != 'X': return
            seen.add((i, j))
            for ii, jj in adj:
                explore(i + ii, j + jj)

        total, n, m, seen = 0, len(grid), len(grid[0]), set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 'X' or (i, j) in seen: continue
                total += 1
                explore(i, j)
        return total


grid = ["OOOXOOO",
     "OOXXOXO",
     "OXOOOXO"]
test = Solution()
print(test.black(grid))
