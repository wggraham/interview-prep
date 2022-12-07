class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        if not A: return

        a = A.split()
        return ' '.join(a[::-1])

A = "     the  sky is blue    "
test = Solution()
print(test.solve(A))