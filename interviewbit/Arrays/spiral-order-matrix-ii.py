class Solution:
    # @param A : integer
    # @return a list of list of integers
    def __init__(self):
        self.m = None
        self.val = 1

    def fillLayer(self, i):
        if i > len(self.m) << 1:
            return False

        n = len(self.m)
        for j in range(i, n-1-i):
            self.m[i][j] = self.val
            self.val += 1
        for j in range(i, n-1-i):
            self.m[j][n-1-i] = self.val
            self.val += 1
        for j in reversed(range(i + 1, n - i)):
            self.m[n-1-i][j] = self.val
            self.val += 1
        for j in reversed(range(i + 1, n - i)):
            self.m[j][i] = self.val
            self.val += 1
        return True

    def generateMatrix(self, A):
        if A <= 0:
            return []

        self.m = [[0] * A for _ in range(A)]
        self.m[A//2][A//2] = A * A
        i = 0
        while True:
            if not self.fillLayer(i):
                break
            i += 1

        return self.m


test = Solution()
print(test.generateMatrix(4))
