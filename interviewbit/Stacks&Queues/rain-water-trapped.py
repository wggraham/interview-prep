class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        if not A or len(A) < 3:
            return 0

        def getTotal(nums):
            total = 0

            j = 0
            for i in range(len(nums)):
                if nums[i] < nums[j]:
                    continue
                total += sum([nums[j] - nums[k] for k in range(j + 1, i)])
                j = i
            return total, j

        total, i = getTotal(A)
        n = len(A)
        if i < (n - 1):
            t, _ = getTotal(A[i:n][::-1])
            total += t
        return total


A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
A = [100, 49, 81, 75, 77, 0, 20, 50, 29, 4, 38, 6, 3, 10, 62, 95, 27, 9, 73, 86, 33, 16, 8, 26, 85, 9, 22, 42, 42, 33,
     28, 95, 46, 46, 62, 78, 92, 91]
test = Solution()
print(test.trap(A))
