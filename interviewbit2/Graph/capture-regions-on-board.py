class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        def inBounds(y, x):
            return 0 <= x < m and 0 <= y < n

        def capture(i, j):
            if A[i][j] == 'X':
                return True
            res, A[i][j] = True, '2'
            for y, x in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if not inBounds(y, x):
                    return False
                if A[y][x] == '2': continue
                res &= capture(y, x)
            if res:
                A[i][j] = 'X'
            return res

        n, m = len(A), len(A[0])
        for i in range(n):
            A[i] = list(A[i])

        for i in range(n):
            for j in range(m):
                if A[i][j] == 'O':
                    A[i][j] = '2'
                    capture(i, j)

        for i in range(n):
            for j in range(m):
                if A[i][j] == '2':
                    A[i][j] = 'O'
        for i in range(n):
            A[i] = ''.join(A[i])

    def solve2(self, A):
        def inBounds(y, x):
            return 0 <= x < m and 0 <= y < n

        def explore(i, j):
            A[i][j] = '2'
            for y, x in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if not inBounds(y, x) or A[y][x] != 'O':
                    continue
                explore(y, x)

        n, m = len(A), len(A[0])
        for i in range(n):
            A[i] = list(A[i])

        for i in range(n):
            if A[i][0] == 'O':
                explore(i, 0)
            if A[i][-1] == 'O':
                explore(i, m - 1)

        for j in range(m):
            if A[0][j] == 'O':
                explore(0, j)
            if A[-1][j] == 'O':
                explore(n - 1, j)

        for i in range(n):
            for j in range(m):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                elif A[i][j] == '2':
                    A[i][j] = 'O'

        for i in range(n):
            A[i] = ''.join(A[i])


A = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
A = ["XOOOOOOX",
     "XXOOXOOX",
     "OXXOXOXX"]
test = Solution()
test.solve(A)
print(10)
