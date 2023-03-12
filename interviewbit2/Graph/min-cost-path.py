from collections import deque
from sys import maxsize


class Solution:
    def solve2(self, n, m, board):
        def inBounds(x, y):
            return 0 <= x < n and 0 <= y < m

        q, move, dp = deque([(0, 0)]), [['D', 1, 0], ['U', -1, 0], ['L', 0, -1], ['R', 0, 1]], \
            [[maxsize] * m for _ in range(n)]
        dp[0][0] = 0
        while q:
            i, j = q.popleft()
            for k in range(4):
                u = (i + move[k][1], j + move[k][2])
                w = (move[k][0] != board[i][j])
                if inBounds(u[0], u[1]):
                    if dp[u[0]][u[1]] > dp[i][j] + w:
                        dp[u[0]][u[1]] = dp[i][j] + w
                        q = q + deque([u]) if w else deque([u]) + q

        return dp[-1][-1]

    # doesn't work
    def solve(self, n, m, board):
        dp = [[maxsize] * m for _ in range(n)]
        dp[0][0] = 0
        for i in range(n):
            board[i] = list(board[i])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: continue
                temp = maxsize
                if 0 < i:
                    temp = min(temp, dp[i - 1][j] + int(board[i - 1][j] != 'D'))
                if 0 < j:
                    temp = min(temp, dp[i][j - 1] + int(board[i][j - 1] != 'R'))
                if i < n - 1:
                    temp = min(temp, dp[i + 1][j] + int(board[i + 1][j] != 'U'))
                if j < m - 1:
                    temp = min(temp, dp[i][j + 1] + int(board[i][j + 1] != 'L'))
                dp[i][j] = temp

        return dp[-1][-1]

    def solve3(self, n, m, board):
        q, visited, cost = deque([(0, 0, 0)]), {(0, 0)}, 0
        while q:
            i, j, cost = q.popleft()
            if i == n - 1 and j == m - 1:
                break
            visited.add((i, j))
            if j + 1 < m and (i, j + 1) not in visited:
                q = deque([(i, j + 1, cost)]) + q if board[i][j] == 'R' else q + deque([(i, j + 1, cost + 1)])
            if i + 1 < n and (i + 1, j) not in visited:
                q = deque([(i + 1, j, cost)]) + q if board[i][j] == 'D' else q + deque([(i + 1, j, cost + 1)])
            if j - 1 >= 0 and (i, j - 1) not in visited:
                q = deque([(i, j - 1, cost)]) + q if board[i][j] == 'L' else q + deque([(i, j - 1, cost + 1)])
            if i - 1 >= 0 and (i - 1, j) not in visited:
                q = deque([(i - 1, j, cost)]) + q if board[i][j] == 'U' else q + deque([(i - 1, j, cost + 1)])

        return cost

    def solve4(self, n, m, board):
        q, visited, cost = deque([(0, 0, 0)]), {(0, 0)}, 0
        while q:
            i, j, cost = q.popleft()
            if i == n - 1 and j == m - 1:
                break
            visited.add((i, j))
            for dir, y, x in [['D', i + 1, j], ['U', i - 1, j], ['L', i, j - 1], ['R', i, j + 1]]:
                if not (0 <= y < n and 0 <= x < m) or (y, x) in visited: continue
                q = deque([(y, x, cost)]) + q if board[i][j] == dir else q + deque([(y, x, cost + 1)])

        return cost


A = 3
B = 3
C = ["RRR", "DDD", "UUU"]
# A = 1
# B = 4
# C = ["LLLL"]
A = 30
B = 30
C = ["LLLDLLRDRLLLLRRDRDDDLDLRRDDDDL", "DLDDLRDLRLLDLDRLLLRRRLDDLLDLRL", "DLRDDLRRLDRRRDLLDRDLRLLDDLRLDL",
     "LLRLLLDDDLRDDLDLLDRLDRLLRRRRLL", "LRLRRDLLDDRDDLRRLLLLLRRRRRRLDL", "DLLRRRLLRRRDDLDRRLLRDRDRDRDLDR",
     "LDRRLLRRRRRDLLDRRDDLRDRDRRRDDD", "DDLDLDDLLDLLLRLDDDLDDDLLDDLRDR", "LLLLRRLDDRRDDRDDRDLLLDDLRRDLDL",
     "DLDDLLDRRDLDLRDDRRRRDDLLRDLRLD", "LLDDLLLDDRDLLRDRRDRLDRLRDRRLDR", "LDDDDRRRRDRRLLDDDDRLDRRDDDRLRR",
     "LRRDRDLRDLRRDLLDRDDLDDDLLLRRLD", "DLDDDLRDRRLRDDRDRDDLRLLRLDRLDR", "LRLDLRRRLLDRLDDRDLRDDRRDRRLLRL",
     "RDLLRDLLLRRRRLDRRDDLDRLLDDLLLD", "RLRLDRLRLDRDDDDRLDRDDLDDDRDDLL", "LDLLRDRRLDDRRLDRLRDDLLLRDLRDDD",
     "LDDLDDLRDRRDRLLRDLDDRLRDLLLRLD", "DDLLLRRLDDRDDRRRDRDLRLDLRDRLRR", "RRRLRRDDDLDRDRLRDRDDRDLLRRLRDR",
     "RLDDRDLLLLRDRRRDDDLDRDDLRLDDRD", "RDRDDDRDDDDLDDRLRLLLRDRLRDLDDL", "DDRLDDDLDLLRDLDRDRRRDRRDRRDLDD",
     "DLRRRLDLRRLDDRLLDLRRDRLLLRRRLR", "LLDRDLRDLLLLDLDLRRLRLLRRLRRLRD", "RLRDLLDLLDLLLDLDRDDRDDRDRDRLRL",
     "DDDLRRLDRLLRRRDDDDLDDRLLRRLLRL", "DDDRRLDLLDRLDLDDDDLLLLDRRDDDDR", "RDLRDLRLDRLRLRRDDLDLRLDDRRLDLR"]

test = Solution()
print(test.solve(A, B, C))
print(test.solve2(A, B, C))
print(test.solve3(A, B, C))
print(test.solve4(A, B, C))
