import math


class Solution:
    def __init__(self):
        self.a = None
        self.n = -1

    def rotate(self, A):

        def rotateElements(i, j):
            n = len(A)
            tmp = A[j][i]
            A[j][i] = A[n-1-j][i]
            A[n-1-j][i] = A[n-1-j][n-1-i]
            A[n - 1 - j][n - 1 - i] = A[j][n-1-i]
            A[j][n-1-i] = tmp

        for j in range(math.ceil(len(A)/2)):
            for i in range(j, len(A)-j - 1):
                rotateElements(i, j)
        return A


a = [
    [1, 2],
    [3, 4]
]

test = Solution()
print(test.rotate(a))
