import time
from math import sqrt


class Solution:
    def isValidSudoku(self, matrix):
        def is_valid_move(i, j, val):
            return val in row[i] and val in col[j] and val in grid[n * (i // n) + (j // n)]

        def make_move(i, j, val):
            row[i].remove(val)
            col[j].remove(val)
            grid[n * (i // n) + (j // n)].remove(val)

        def unmake_move(i, j, val):
            row[i].add(val)
            col[j].add(val)
            grid[n * (i // n) + (j // n)].add(val)

        def get_possible_moves(i, j):
            return row[i].intersection(col[j], grid[n * (i // n) + (j // n)])

        def get_cell():
            min_moves, min_cell = None, None
            for cell in open_cells:
                moves = get_possible_moves(cell[0], cell[1])
                if not min_moves or len(moves) < len(min_moves):
                    min_cell = cell
                    min_moves = moves

            return min_cell, min_moves

        def try_move():
            if not open_cells:
                return True

            while open_cells:
                cell, moves = get_cell()
                open_cells.remove(cell)
                for move in moves:
                    make_move(cell[0], cell[1], move)
                    valid = try_move()
                    if valid:
                        return valid
                    else:
                        unmake_move(cell[0], cell[1], move)
            return False

        n = len(matrix)
        row = [{x for x in range(1, n + 1)} for _ in range(n)]
        col = [{x for x in range(1, n + 1)} for _ in range(n)]
        grid = [{x for x in range(1, n + 1)} for _ in range(n)]
        open_cells = set()

        for i in range(n):
            for j, cell in enumerate(matrix[i]):
                if cell == '.':
                    open_cells.add((i, j))
                elif is_valid_move(i, j, int(cell)):
                    make_move(i, j, int(cell))
                else:
                    return 0

        return 1 if try_move() else 0

    def isValidSudoku2(self, A):
        for i in range(9):
            if not self.isValidArray(list(A[i])) \
                    or not self.isValidArray([A[j][i] for j in range(9)]) \
                    or not self.isValidArray([A[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] for j in range(9)]):
                return 0
        return 1

    def isValidArray(self, arr):
        s = set()
        for x in arr:
            if x in s:
                return False
            if x != '.':
                s.add(x)
        return True

    def isValidSudoku3(self, matrix):
        def is_valid_move(i, j, val):
            return all(val not in x for x in (row[i], col[j], grid[m * (i // m) + (j // m)]))

        def make_move(i, j, val):
            for x in (row[i], col[j], grid[m * (i // m) + (j // m)]):
                x.add(val)

        n = len(matrix)
        m = int(sqrt(n))
        row, col, grid = [set() for _ in range(n)], [set() for _ in range(n)], [set() for _ in range(n)]

        for i in range(n):
            for j, cell in enumerate(matrix[i]):
                if cell == '.': continue
                if not is_valid_move(i, j, int(cell)):
                    return 0

                make_move(i, j, int(cell))

        return 1


matrix = ["53.17....",
          "6..195...",
          ".98....6.",
          "8...6...3",
          "4..8.3..1",
          "7...2...6",
          ".6....28.",
          "...419..5",
          "....8..79"]
A = ["....5..1.",
     ".4.3.....",
     ".....3..1",
     "8......2.",
     "..2.7....",
     ".15......",
     ".....2...",
     ".2.9.....",
     "..4......"]
A = ["..5.....6",
     "....14...",
     ".........",
     ".....92..",
     "5....2...",
     ".......3.",
     "...54....",
     "3.....42.",
     "...27.6.."]

test = Solution()
t0 = time.time()
print(test.isValidSudoku2(A))
test.isValidSudoku2(matrix)
t1 = time.time()
print(test.isValidSudoku3(A))
test.isValidSudoku3(matrix)
t2 = time.time()
print("mine: ", t2 - t1)
print("theirs: ", t1 - t0)
