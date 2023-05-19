import string
from typing import List


class Solution:

    def solveSudoku1(self, board: List[List[str]]) -> None:
        def solve(free):
            if not free:
                return True

            cell, choices = None, None
            for y, x in free:
                values = {d for d in string.digits[1:]}
                for i in range(n):
                    if board[y][i] != '.' and board[y][i] in values:
                        values.remove(board[y][i])
                    if board[i][x] != '.' and board[i][x] in values:
                        values.remove(board[i][x])
                    if board[y // 3 * 3 + i % 3][x // 3 * 3 + i // 3] != '.' and \
                            board[y // 3 * 3 + i % 3][x // 3 * 3 + i // 3] in values:
                        values.remove(board[y // 3 * 3 + i % 3][x // 3 * 3 + i // 3])
                if not values:
                    return False
                if not choices or len(values) < len(choices):
                    choices = values
                    cell = (y, x)

            for d in choices:
                board[cell[0]][cell[1]] = d
                free.remove(cell)
                if solve(free):
                    return True
                board[cell[0]][cell[1]] = '.'
                free.add(cell)

            return False

        n, open_cells = len(board), set()
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    open_cells.add((i, j))

        solve(open_cells)

    def solveSudoku(self, board: List[List[str]]) -> None:
        def solve(free):
            if not free:
                return True
            choices, cell = None, None
            for y, x in free:
                values = rows[y].intersection(cols[x]).intersection(grids[3 * (y // 3) + x // 3])
                if not values:
                    return False
                if not choices or len(values) < len(choices):
                    choices = values
                    cell = (y, x)

            for d in choices:
                board[cell[0]][cell[1]] = d
                rows[cell[0]].remove(d)
                cols[cell[1]].remove(d)
                grids[3 * (cell[0] // 3) + cell[1] // 3].remove(d)
                free.remove(cell)
                if solve(free): return True
                board[cell[0]][cell[1]] = '.'
                rows[cell[0]].add(d)
                cols[cell[1]].add(d)
                grids[3 * (cell[0] // 3) + cell[1] // 3].add(d)
                free.add(cell)

            return False

        n, open_cells = len(board), set()
        rows = [{d for d in string.digits[1:]} for _ in range(n)]
        cols = [{d for d in string.digits[1:]} for _ in range(n)]
        grids = [{d for d in string.digits[1:]} for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    rows[i].remove(board[i][j])
                    cols[j].remove(board[i][j])
                    grids[3 * (i // 3) + j // 3].remove(board[i][j])
                else:
                    open_cells.add((i, j))

        solve(open_cells)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test = Solution()
test.solveSudoku1(board)
print(board)
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test.solveSudoku(board)
print(board)
