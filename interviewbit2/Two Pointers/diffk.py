class Solution:
    def diffPossible(self, A, B):
        i, j = 0, 1
        while j < len(A):
            while j < len(A) - 1 and A[j] - A[i] < B:
                j += 1
            if A[j] - A[i] == B:
                return 1
            i += 1
            j += 1 if i == j else 0

        return 0


A = [1, 3, 5]
B = 6
A = [1, 2, 2, 3, 4]
B = 0
test = Solution()
print(test.diffPossible(A, B))
