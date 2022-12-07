class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        common = []
        i, j = 0, 0
        n, m = len(A), len(B)
        while i < n and j < m:
            while i < n and j < m and A[i] == B[j]:
                common.append(A[i])
                i += 1
                j += 1
            if i < n and j < m and A[i] < B[j]:
                i += 1
            else:
                j += 1

        return common


A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5]
test = Solution()
print(test.intersect(A, B))

