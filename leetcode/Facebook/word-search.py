import itertools
import time
from typing import List


class Solution:
    # TLE, otherwise need to transfer entire board state to each recursive call
    # to ensure (i, j, k) already seen has not been encountered from another set
    # of visited cells, multiple paths of length k leading to same position
    def exist(self, board: List[List[str]], word: str) -> bool:
        def inBound(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(i, j, k, used):
            if not inBound(i, j) or (i, j) in used or board[i][j] != word[k]:
                return False
            if k == w_len - 1:
                return True

            return any(
                explore(i + ii, j + jj, k + 1, used.union({(i, j)})) for ii, jj in [(0, -1), (0, 1), (1, 0), (-1, 0)])

        n, m, w_len = len(board), len(board[0]), len(word)
        return any(explore(i, j, 0, set()) for j in range(m) for i in range(n))

    def exist2(self, board, word):
        def backtrack(i, j, suffix):
            if not len(suffix):
                return True

            if not (0 <= i < n and 0 <= j < m) or board[i][j] != suffix[0]:
                return False

            board[i][j] = '#'
            for ii, jj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = backtrack(i + ii, j + jj, suffix[1:])
                if ret: break

            board[i][j] = suffix[0]

            return ret

        n, m = len(board), len(board[0])
        return any(backtrack(i, j, word) for i, j in itertools.product(range(n), range(m)))

    def exist3(self, board: List[List[str]], word: str) -> bool:
        def inBound(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(i, j, k, used):
            if not inBound(i, j) or (i, j) in used or board[i][j] != word[k]:
                return False
            if k == w_len - 1:
                return True
            used.add((i, j))
            for ii, jj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                found = explore(i + ii, j + jj, k + 1, used)
                if found: break
            used.remove((i, j))
            return found

        n, m, w_len, found = len(board), len(board[0]), len(word), False
        for i, j in itertools.product(range(n), range(m)):
            if board[i][j] != word[0]: continue
            found = explore(i, j, 0, set())
            if found: break
        return found

    def exist4(self, board: List[List[str]], word: str) -> bool:
        def explore(i, j, k, used):
            if not (0 <= i < n and 0 <= j < m) or (i, j) in used or board[i][j] != word[k]:
                return False
            if k == w_len - 1:
                return True
            used.add((i, j))
            for ii, jj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                found = explore(i + ii, j + jj, k + 1, used)
                if found: break
            used.remove((i, j))
            return found

        n, m, w_len = len(board), len(board[0]), len(word)
        # for i, j in itertools.product(range(n), range(m)):
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]: continue
                found = explore(i, j, 0, set())
                if found:
                    return True
        return False

    def exist5(self, board: List[List[str]], word: str) -> bool:
        def explore(i, j, k, used):
            if not (0 <= i < n and 0 <= j < m) or (i, j) in used or board[i][j] != word[k]:
                return False
            if k == w_len - 1:
                return True
            used.add((i, j))
            for ii, jj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                found = explore(i + ii, j + jj, k + 1, used)
                if found: break
            used.remove((i, j))
            return found

        n, m, w_len, found = len(board), len(board[0]), len(word), False
        for i, j in itertools.product(range(n), range(m)):
            if board[i][j] != word[0]: continue
            found = explore(i, j, 0, set())
            if found: break

        return found

    def exist6(self, board, word):
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True

            if row < 0 or row == n or col < 0 or col == m \
                    or board[row][col] != suffix[0]:
                return False

            board[row][col] = '#'
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = backtrack(row + rowOffset, col + colOffset, suffix[1:])
                if ret: break

            board[row][col] = suffix[0]

            return ret

        n, m = len(board), len(board[0])

        for row in range(n):
            for col in range(m):
                if backtrack(row, col, word):
                    return True

        return False

    def exist7(self, board: List[List[str]], word: str) -> bool:
        def explore(i, j, k, used):
            if k == w_len - 1:
                return True
            found = False
            used.add((i, j))
            for ii, jj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                y, x = i + ii, j + jj
                if not (0 <= y < n and 0 <= x < m) or (y, x) in used or board[y][x] != word[k + 1]: continue
                found = explore(y, x, k + 1, used)
                if found: break
            used.remove((i, j))
            return found

        n, m, w_len, found = len(board), len(board[0]), len(word), False
        for i, j in itertools.product(range(n), range(m)):
            if board[i][j] != word[0]: continue
            found = explore(i, j, 0, set())
            if found: break

        return found


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
# board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
# word = "ABCESEEEFS"
board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
word = "AAAAAAAAAAAAABB"

# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
test = Solution()
# t0 = time.time()
# test.exist(board, word)
# t1 = time.time()
# test.exist2(board, word)
# t2 = time.time()
# test.exist3(board, word)
# t3 = time.time()
# test.exist4(board, word)
t4 = time.time()
(test.exist5(board, word))
t5 = time.time()
(test.exist6(board, word))
t6 = time.time()
(test.exist7(board, word))
t7 = time.time()
# print("original: ", t1 - t0)
# print("theirs: ", t2 - t1)
# print("mine sped up: ", t3 - t2)
# print("mine sped up2: ", t4 - t3)
print("mine sped up3: ", t5 - t4)
print("theirs og: ", t6 - t5)
print("mine sped up4: ", t7 - t6)
