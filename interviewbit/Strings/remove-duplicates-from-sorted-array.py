class Solution:
    def removeDuplicates(self, A):
        if not A or len(A) < 2:
            return 0

        b, f = 0, 1
        while f < len(A):
            while f < len(A) and A[b] == A[f]:
                f += 1
            A[b] = A[f - 1]
            b += 1
            if f < len(A):
                A[b] = A[f]

        A = A[:b+1]
        if A[-1] == A[b]:
            A = A[:-1]
        return len(A)


test = Solution()
a = [0]
print(test.removeDuplicates(a))
