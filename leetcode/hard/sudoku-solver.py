from typing import List


class Solution:
    def __init__(self):
        self.open = set()
        self.grid = [{str(x) for x in range(1, 10)} for _ in range(9)]
        self.row = [{str(x) for x in range(1, 10)} for _ in range(9)]
        self.col = [{str(x) for x in range(1, 10)} for _ in range(9)]
        self.board = None

    def initParams(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    self.open.add((i, j))
                else:
                    self.row[i].remove(self.board[i][j])
                    self.col[j].remove(self.board[i][j])
                    self.grid[i // 3 * 3 + j // 3].remove(self.board[i][j])

    def make(self, i, j, val):
        self.board[i][j] = val
        self.open.remove((i, j))
        self.row[i].remove(val)
        self.col[j].remove(val)
        self.grid[i // 3 * 3 + j // 3].remove(val)

    def unmake(self, i, j, val):
        self.board[i][j] = '.'
        self.open.add((i, j))
        self.row[i].add(val)
        self.col[j].add(val)
        self.grid[i // 3 * 3 + j // 3].add(val)

    def getPossibleValues(self, i, j):
        return self.row[i].intersection(self.col[j], self.grid[i // 3 * 3 + j // 3])

    def check(self, y, x, val):
        gval = y // 3 * 3 + x // 3
        for i in range(9):
            for j in range(9):
                if i == y and j == x: continue
                if (i, j) not in self.open: continue
                if i == y or j == x or i // 3 * 3 + j // 3 == gval:
                    vals = self.getPossibleValues(i, j)
                    if not vals or (len(vals) == 1 and val in vals):
                        return False
        return True

    def getCell(self):
        cell = None
        choices = None
        minVal = 9
        for c in self.open:
            i, j = c
            vals = self.getPossibleValues(i, j)
            if len(vals) and len(vals) < minVal:
                minVal = len(vals)
                cell = c
                choices = vals
        return cell, choices

    def solve(self):
        cell, vals = self.getCell()
        if not vals: return
        for val in vals:
            if self.check(cell[0], cell[1], val):
                self.make(cell[0], cell[1], val)
                self.solve()

                if not len(self.open):
                    return

                self.unmake(cell[0], cell[1], val)

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.initParams()

        self.solve()
        return


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
test = Solution()
test.solveSudoku(board)
print(board)
