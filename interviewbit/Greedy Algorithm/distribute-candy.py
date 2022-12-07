class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        if n == 0: return 0
        if n < 2: return 1

        left, right = [1] * n, [1] * n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                left[i] += left[i - 1]
        for i in reversed(range(n-1)):
            if A[i] > A[i + 1]:
                right[i] += right[i + 1]

        return sum([max(left[i], right[i]) for i in range(n)])


a = [1, 5, 2, 1]
test = Solution()
print(test.candy(a))
