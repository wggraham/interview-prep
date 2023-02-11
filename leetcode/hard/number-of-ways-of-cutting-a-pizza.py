from functools import lru_cache
from time import time
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @lru_cache(None)
        def count_ways(y, x, cuts):
            if not cuts: return 1
            count = 0
            for i in range(x, n - 1):
                if 0 < suffix_sum[i + 1][y] < suffix_sum[x][y]:
                    count += count_ways(y, i + 1, cuts - 1)
            for j in range(y, m - 1):
                if 0 < suffix_sum[x][j + 1] < suffix_sum[x][y]:
                    count += count_ways(j + 1, x, cuts - 1)

            return count % mod

        n, m, mod = len(pizza), len(pizza[0]), (10 ** 9) + 7
        suffix_sum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                suffix_sum[i][j] = int(pizza[i][j] == 'A') \
                                   + suffix_sum[i + 1][j] \
                                   + suffix_sum[i][j + 1] \
                                   - suffix_sum[i + 1][j + 1]

        return count_ways(0, 0, k - 1)

    def ways2(self, grid, k):
        def count(a, b, c, d):
            return sum_grid[c][d] - sum_grid[a][d] \
                - sum_grid[c][b] + sum_grid[a][b]

        def dfs(a, b, k):
            if (a, b, k) in dp: return dp[(a, b, k)]
            if k == 1 and count(a, b, n, m) >= 1: return 1

            ret, mod = 0, int(1e9 + 7)
            for i in range(a + 1, n):
                if count(a, b, i, m) >= 1:
                    ret = (ret + dfs(i, b, k - 1)) % mod
            for j in range(b + 1, m):
                if count(a, b, n, j) >= 1:
                    ret = (ret + dfs(a, j, k - 1)) % mod
            dp[(a, b, k)] = ret
            return ret

        n, m = len(grid), len(grid[0])
        N, M = n + 1, m + 1
        sum_grid = [[0] * M for _ in range(N)]
        for i in range(1, N):
            for j in range(1, M):
                sum_grid[i][j] = sum_grid[i - 1][j] + sum_grid[i][j - 1] \
                                 - sum_grid[i - 1][j - 1] + int(grid[i - 1][j - 1] == 'A')

        dp = {}
        return dfs(0, 0, k)


pizza = ["A..A.", "A..A.", "A..A.", "A..A.", "A..A.", "AA.AA", "..A..", ".AA.A", ".A.A."]
k = 3
pizza = ["..A.A.AAA...AAAAAA.AA..A..A.A......A.AAA.AAAAAA.AA", "A.AA.A.....AA..AA.AA.A....AAA.A........AAAAA.A.AA.",
         "A..AA.AAA..AAAAAAAA..AA...A..A...A..AAA...AAAA..AA", "....A.A.AA.AA.AA...A.AA.AAA...A....AA.......A..AA.",
         "AAA....AA.A.A.AAA...A..A....A..AAAA...A.A.A.AAAA..", "....AA..A.AA..A.A...A.A..AAAA..AAAA.A.AA..AAA...AA",
         "A..A.AA.AA.A.A.AA..A.A..A.A.AAA....AAAAA.A.AA..A.A", ".AA.A...AAAAA.A..A....A...A.AAAA.AA..A.AA.AAAA.AA.",
         "A.AA.AAAA.....AA..AAA..AAAAAAA...AA.A..A.AAAAA.A..", "A.A...A.A...A..A...A.AAAA.A..A....A..AA.AAA.AA.AA.",
         ".A.A.A....AAA..AAA...A.AA..AAAAAAA.....AA....A....", "..AAAAAA..A..A...AA.A..A.AA......A.AA....A.A.AAAA.",
         "...A.AA.AAA.AA....A..AAAA...A..AAA.AAAA.A.....AA.A", "A.AAAAA..A...AAAAAAAA.AAA.....A.AAA.AA.A..A.A.A...",
         "A.A.AA...A.A.AA...A.AA.AA....AA...AA.A..A.AA....AA", "AA.A..A.AA..AAAAA...A..AAAAA.AA..AA.AA.A..AAAAA..A",
         "...AA....AAAA.A...AA....AAAAA.A.AAAA.A.AA..AA..AAA", "..AAAA..AA..A.AA.A.A.AA...A...AAAAAAA..A.AAA..AA.A",
         "AA....AA....AA.A......AAA...A...A.AA.A.AA.A.A.AA.A", "A.AAAA..AA..A..AAA.AAA.A....AAA.....A..A.AA.A.A...",
         "..AA...AAAAA.A.A......AA...A..AAA.AA..A.A.A.AA..A.", ".......AA..AA.AAA.A....A...A.AA..A.A..AAAAAAA.AA.A",
         ".A.AAA.AA..A.A.A.A.A.AA...AAAA.A.A.AA..A...A.AAA..", "A..AAAAA.A..A..A.A..AA..A...AAA.AA.A.A.AAA..A.AA..",
         "A.AAA.A.AAAAA....AA..A.AAA.A..AA...AA..A.A.A.AA.AA", ".A..AAAA.A.A.A.A.......AAAA.AA...AA..AAA..A...A.AA",
         "A.A.A.A..A...AA..A.AAA..AAAAA.AA.A.A.A..AA.A.A....", "A..A..A.A.AA.A....A...A......A.AA.AAA..A.AA...AA..",
         ".....A..A...A.A...A..A.AA.A...AA..AAA...AA..A.AAA.", "A...AA..A..AA.A.A.AAA..AA..AAA...AAA..AAA.AAAAA...",
         "AA...AAA.AAA...AAAA..A...A..A...AA...A..AA.A...A..", "A.AA..AAAA.AA.AAA.A.AA.A..AAAAA.A...A.A...A.AA....",
         "A.......AA....AA..AAA.AAAAAAA.A.AA..A.A.AA....AA..", ".A.A...AA..AA...AA.AAAA.....A..A..A.AA.A.AA...A.AA",
         "..AA.AA.AA..A...AA.AA.AAAAAA.....A.AA..AA......A..", "AAA..AA...A....A....AA.AA.AA.A.A.A..AA.AA..AAA.AAA",
         "..AAA.AAA.A.AA.....AAA.A.AA.AAAAA..AA..AA.........", ".AA..A......A.A.AAA.AAAA...A.AAAA...AAA.AAAA.....A",
         "AAAAAAA.AA..A....AAAA.A..AA.A....AA.A...A.A....A..", ".A.A.AA..A.AA.....A.A...A.A..A...AAA..A..AA..A.AAA",
         "AAAA....A...A.AA..AAA..A.AAA..AA.........AA.AAA.A.", "......AAAA..A.AAA.A..AAA...AAAAA...A.AA..A.A.AA.A.",
         "AA......A.AAAAAAAA..A.AAA...A.A....A.AAA.AA.A.AAA.", ".A.A....A.AAA..A..AA........A.AAAA.AAA.AA....A..AA",
         ".AA.A...AA.AAA.A....A.A...A........A.AAA......A...", "..AAA....A.A...A.AA..AAA.AAAAA....AAAAA..AA.AAAA..",
         "..A.AAA.AA..A.AA.A...A.AA....AAA.A.....AAA...A...A", ".AA.AA...A....A.AA.A..A..AAA.A.A.AA.......A.A...A.",
         "...A...A.AA.A..AAAAA...AA..A.A..AAA.AA...AA...A.A.", "..AAA..A.A..A..A..AA..AA...A..AA.AAAAA.A....A..A.A"]
k = 8
test = Solution()
t0 = time()
for i in range(1):
    test.ways(pizza, k)
t1 = time()
for i in range(1):
    test.ways2(pizza, k)
t2 = time()

print(t1 - t0)
print(t2 - t1)
