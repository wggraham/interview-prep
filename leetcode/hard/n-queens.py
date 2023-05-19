from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(i, cols, diag_inc, diag_dec, board):
            if i == n:
                res.append(board)
                return
            for j in range(n):
                if j in cols:
                    continue
                if i - j in diag_inc:
                    continue
                if i + j in diag_dec:
                    continue
                cols.add(j)
                diag_inc.add(i - j)
                diag_dec.add(i + j)
                solve(i + 1, cols, diag_inc, diag_dec, board + [''.join(['.' if k != j else 'Q' for k in range(n)])])
                cols.remove(j)
                diag_inc.remove(i - j)
                diag_dec.remove(i + j)

        res = []
        solve(0, set(), set(), set(), [])
        return res


test = Solution()
print(test.solveNQueens(4))
