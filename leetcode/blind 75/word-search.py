from typing import List
from copy import copy


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, o = len(board), len(board[0]), len(word)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def inBounds(i, j):
            nonlocal n, m
            return 0 <= i < n and 0 <= j < m

        def explore(i, j):
            nonlocal board, word, n, m, o, directions
            s = [(i, j, 1, {(i, j)})]

            while s:
                i, j, k, d = s.pop()
                if k == o:
                    return True
                for ii, jj in directions:
                    y, x = i + ii, j + jj
                    if not inBounds(y, x) or board[y][x] != word[k] or (y, x) in d:
                        continue
                    d.add((y, x))
                    s.append((y, x, k + 1, copy(d)))
                    d.remove((y, x))
            return False

        for i in range(n):
            for j in range(m):
                if not board[i][j] == word[0]:
                    continue
                found = explore(i, j)
                if found:
                    return found
        return False


test = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(test.exist(board, word))
