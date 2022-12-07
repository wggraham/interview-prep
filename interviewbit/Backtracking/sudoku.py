class Solution:
    def solveSudoku(self, A):
        if not A: return

        def initSets(A):
            r = [set() for _ in A]
            c = [set() for _ in A]
            g = [set() for _ in A]

            for i in range(len(A)):
                for j in range(len(A[i])):
                    if A[i][j] == '.':
                        continue

                    r[i].add(A[i][j])
                    c[j].add(A[i][j])
                    g[i // 3 * 3 + j // 3].add(A[i][j])
            return r, c, g

        def getOpenCells(A):
            s = set()
            for i in range(len(A)):
                for j in range(len(A[i])):
                    if A[i][j] == '.':
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
                A[i][j] = v
                if solve(openCells, rows, cols, grids):
                    return True
                if v in rows[i]:
                    rows[i].remove(v)
                if v in cols[j]:
                    cols[j].remove(v)
                if v in grids[i // 3 * 3 + j // 3]:
                    grids[i // 3 * 3 + j // 3].remove(v)
                openCells.add((i, j))
                A[i][j] = '.'
            return False

        A = [list(s) for s in A]
        r, c, g = initSets(A)
        oc = getOpenCells(A)

        solve(oc, r, c, g)
        return A


t = ["53..7....",
     "6..195...",
     ".98....6.",
     "8...6...3",
     "4..8.3..1",
     "7...2...6",
     ".6....28.",
     "...419..5",
     "....8..79"]

test = Solution()
print(test.solveSudoku(t))
