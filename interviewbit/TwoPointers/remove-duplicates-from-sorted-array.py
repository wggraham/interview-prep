class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A or len(A) < 2:
            return 0

        def getNextIdx(i):
            nonlocal A, n
            j = i + 1

            while j < n and A[j] == A[i]:
                j += 1
            return j

        s, e, n = 0, 0, len(A)
        while e < n:
            e = getNextIdx(e)
            A[s] = A[e - 1]
            s += 1

        return len(A[:s])


test = Solution()
A = [1, 2, 2, 3, 3]
print(test.removeDuplicates(A))
