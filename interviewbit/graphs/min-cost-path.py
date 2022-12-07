from sys import maxsize


class Solution:
    def solve(self, A, B, C):
        if not C: return
        n, m = len(C), len(C[0])

        dp = [[maxsize] * m for _ in C]
        dirMap = {'D': (-1, 0), 'U': (1, 0), 'L': (0, 1), 'R': (0, -1)}
        dp[0][0] = 0
        def inBounds(y, x):
            nonlocal n, m
            return 0 <= x < m and 0 <= y < n

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                t = maxsize
                for k, v in dirMap.items():
                    y, x = i + v[0], j + v[1]
                    if not inBounds(y, x): continue

                    val = dp[y][x] + 1 if C[y][x] is not k else dp[y][x]
                    t = min(t, val)

                dp[i][j] = t

        return dp[-1][-1]


# A = 3
# B = 3
# C = ["RRR","DDD","UUU"]

A = 1
B = 4
C = ["LLLL"]
A = 5
B = 5
C = [ "RRRRD", "DLLLL", "RRRRD", "DLLLL", "RRRRR" ]
test = Solution()
print(test.solve(A,B,C))
