class Solution:
    def explore(self, A, visited, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return
        if A[i][j] == 'X':
            return
        if (i, j) in visited:
            return
        visited.add((i, j))
        self.explore(A, visited, i - 1, j)
        self.explore(A, visited, i + 1, j)
        self.explore(A, visited, i, j - 1)
        self.explore(A, visited, i, j + 1)

    def exploreBorders(self, A, visited):
        # top & bottom edge
        for i in range(len(A[0])):
            if A[0][i] == 'O' and (0, i) not in visited:
                self.explore(A, visited, 0, i)
            if A[len(A)-1][i] == 'O' and (len(A)-1, i) not in visited:
                self.explore(A, visited, len(A)-1, i)

        # left & right edge
        for i in range(len(A)):
            if A[i][0] == 'O' and (i, 0) not in visited:
                self.explore(A, visited, i, 0)
            if A[i][len(A[0])-1] == 'O' and (i, len(A[0])-1) not in visited:
                self.explore(A, visited, i, len(A[0])-1)

    # @param A : list of list of chars
    def solve(self, A):
        visited = set()

        self.exploreBorders(A, visited)
        for i in range(1, len(A) - 1):
            for j in range(1, len(A[0]) - 1):
                if A[i][j] == 'O' and (i, j) not in visited:
                    A[i][j] = 'X'
