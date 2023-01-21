import time


class Solution:
    def solveNQueens(self, A):
        def gen_board(points):
            return [''.join('Q' if (i, j) in points else '.' for i in range(A)) for j in range(A)]

        def solve(i, cols, diags1, diags2, points):
            if i == A:
                res.append(gen_board(points))
                return
            for j in range(A):
                if j in cols or (i - j) in diags2 or (i + j) in diags1:
                    continue
                solve(i + 1, cols.union({j}), diags1.union({i + j}), diags2.union({i - j}), points.union({(i, j)}))

        res = []
        solve(0, set(), set(), set(), set())
        return res

    def solveNQueens1(self, n):
        def solve(i, cols, diags1, diags2, points):
            if i == n:
                res.append([''.join('Q' if (i, j) in points else '.' for i in range(n)) for j in range(n)])
                return
            for j in range(n):
                if j in cols or i - j in diags2 or i + j in diags1:
                    continue
                solve(i + 1, cols.union({j}), diags1.union({i + j}), diags2.union({i - j}), points.union({(i, j)}))

        res = []
        solve(0, set(), set(), set(), set())
        return res

    def solveNQueens11(self, n):
        def solve(i, cols, diags1, diags2, points):
            if i == n:
                res.append([''.join('Q' if (i, j) in points else '.' for i in range(n)) for j in range(n)])
                return
            for j in range(n):
                if j in cols or (i - j) in diags2 or (i + j) in diags1:
                    continue
                cols.add(j)
                diags1.add(i + j)
                diags2.add(i - j)
                points.add((i, j))
                solve(i + 1, cols, diags1, diags2, points)
                cols.remove(j)
                diags1.remove(i + j)
                diags2.remove(i - j)
                points.remove((i, j))

        res = []
        solve(0, set(), set(), set(), set())
        return res

    def solveNQueens2(self, A):
        stack, res, n = [[(0, i)] for i in range(A)], [], A
        while stack:
            board = stack.pop()
            row = len(board)
            if row == n:
                res.append([''.join('Q' if i == c else '.' for i in range(n))
                            for r, c in board])
            for col in range(n):
                if all(col != c and abs(row - r) != abs(col - c) for r, c in board):
                    stack.append(board + [(row, col)])
        return res

    def solveNQueens3(self, n):
        def trace(i):
            if i == n:
                res.append(['.' * j + 'Q' + '.' * (n - j - 1) for j in row])

            for j in range(n):
                if col[j] or diag1[i + j] or diag2[i - j + n]:
                    continue
                col[j] = diag1[i + j] = diag2[i - j + n] = True
                row.append(j)
                trace(i + 1)
                col[j] = diag1[i + j] = diag2[i - j + n] = False
                row.pop()

        row, res, col, diag1, diag2 = [], [], [False] * n, [False] * (2 * n), [False] * (2 * n)
        trace(0)
        return res


test = Solution()
print(sorted(test.solveNQueens11(4)))
print(sorted(test.solveNQueens3(4)))

# t0 = time.time()
# [test.solveNQueens11(12) for _ in range(1)]
# t1 = time.time()
# [test.solveNQueens3(12) for _ in range(1)]
# t2 = time.time()

# print("mine: ", t1 - t0)
# print("theirs: ", t2 - t1)
