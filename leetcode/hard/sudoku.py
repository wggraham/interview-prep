from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        if not board: return

        def initSets(board):
            r = [set() for _ in board]
            c = [set() for _ in board]
            g = [set() for _ in board]

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '.':
                        continue

                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    g[i // 3 * 3 + j // 3].add(board[i][j])
            return r, c, g

        def getOpenCells(board):
            s = set()
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '.':
                        s.add((i, j))
            return s

        def getOptions(i, j, rows, cols, grids):
            s = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            return s.difference(rows[i].union(cols[j]).union(grids[i // 3 * 3 + j // 3]))

        def getMostConstrainedCell(openCells, rows, cols, grids):
            least = 100
            for c in openCells:
                options = getOptions(c[0], c[1], rows, cols, grids)
                if len(options) < least:
                    least = len(options)
                    op = options
                    cell = (c[0], c[1])
            return cell[0], cell[1], op

        def solve(openCells, rows, cols, grids):
            if not openCells:
                return True

            i, j, options = getMostConstrainedCell(openCells, rows, cols, grids)

            for v in options:
                rows[i].add(v)
                cols[j].add(v)
                grids[i // 3 * 3 + j // 3].add(v)
                openCells.remove((i, j))
                board[i][j] = v
                if solve(openCells, rows, cols, grids):
                    return True
                if v in rows[i]:
                    rows[i].remove(v)
                if v in cols[j]:
                    cols[j].remove(v)
                if v in grids[i // 3 * 3 + j // 3]:
                    grids[i // 3 * 3 + j // 3].remove(v)
                openCells.add((i, j))
                board[i][j] = '.'
            return False

        r, c, g = initSets(board)
        oc = getOpenCells(board)

        solve(oc, r, c, g)
        return board


b = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
test = Solution()
print(test.solveSudoku(b))
