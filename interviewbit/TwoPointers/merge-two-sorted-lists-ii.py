class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        n, m = len(A), len(B)
        A += [0] * len(B)

        i, j, k = n - 1, m - 1, n + m - 1
        while j >= 0:
            A[k] = A[i] if A[i] > B[j] else B[j]
            if i >= 0 and A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        return A


A = [1, 2]
B = [-1, 2]
test = Solution()
print(test.merge(A, B))
