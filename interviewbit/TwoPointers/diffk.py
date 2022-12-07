class Solution:
    def diffPossible(self, A, B):
        j = 0
        for i, v in enumerate(A[1:], 1):
            while j < i - 1 and v - A[j] - B > 0:
                j += 1
            if v - A[j] - B == 0:
                return 1
        return 0


A = [1, 2, 3]
B = 0
test = Solution()
print(test.diffPossible(A, B))
