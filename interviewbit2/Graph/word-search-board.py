class Solution:
    def exist(self, board, word):
        def inBounds(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(i, j, k):
            if k == o - 1:
                return True
            found = False
            for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not inBounds(y, x): continue
                if board[y][x] != word[k + 1]: continue
                found |= explore(y, x, k + 1)
            return found

        o, n, word = len(word), len(board), list(word)
        for i in range(n):
            board[i] = list(board[i])
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]: continue
                if explore(i, j, 0):
                    return 1

        return 0

    def exist2(self, board, word):
        def inBounds(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(i, j, k):
            if (i, j, k) in visited:
                return False
            if k == o - 1:
                return True
            found = False
            for y, x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not inBounds(y, x): continue
                if board[y][x] != word[k + 1]: continue
                found |= explore(y, x, k + 1)

            visited.add((i, j, k))
            return found

        o, n, word = len(word), len(board), list(word)
        visited = set()
        for i in range(n):
            board[i] = list(board[i])
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]: continue
                if explore(i, j, 0):
                    return 1

        return 0


board = [
    ["ABCE"],
    ["SFCS"],
    ["ADEE"]
]
word = "ABCCED"
word = "ABCD"
A = ["FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF"]
B = "BCDCB"

test = Solution()
print(test.exist(A, B))
