from copy import copy

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        grid = [['.']*A for _ in range(A)]

        r = set([x for x in range(1, A+1)])
        c = set([x for x in range(1, A+1)])
        lDiag = set([x + 1 for x in range(2*A-1)])
        rDiag = set([x + 1 for x in range(2 * A - 1)])
        res = []
        def getValidQueens(row, col, lDiag, rDiag, grid):
            if not row and not col:
                res.append([''.join(y for y in x) for x in grid])
            for i in row:
                for j in col:
                    ld = i + j - 1
                    rd = (A - i) + (A - j)
                    if ld in lDiag and rd in rDiag:
                        r = copy(row)
                        r.remove(i)
                        c = copy(col)
                        c.remove(j)
                        l = copy(lDiag)
                        l.remove(ld)
                        rr = copy(rDiag)
                        rr.remove(rd)
                        grid[i - 1][j - 1] = 'Q'
                        getValidQueens(r, c, l, rr, grid)
                        grid[i - 1][j - 1] = '.'

        getValidQueens(r, c, lDiag, rDiag, grid)
        return res


n = 4
test = Solution()
print(test.solveNQueens(n))