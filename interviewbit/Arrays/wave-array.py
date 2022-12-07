class Solution:
    def wave(self, A):
        A.sort()

        for i in range(1, len(A)):
            if (i % 2 and A[i] > A[i - 1]) or (not i % 2 and A[i] < A[i - 1]):
                A[i], A[i - 1] = A[i - 1], A[i]
        return A


test = Solution()
A = [2, 3, 1, 4]
print(test.wave(A))



