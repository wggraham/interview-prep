class Solution:
    def solve(self, A):
        return ' '.join(A.split()[::-1])

    def solve2(self, A):
        return ' '.join([word[::-1] for word in A[::-1].split()])

    def solve3(self, A):
        return ' '.join([word[::-1] for word in A.split()])[::-1]

    def solve4(self, A):
        return ' '.join([word for word in A.split()][::-1])


A = "the sky is blue"
test = Solution()
print(test.solve(A))
print(test.solve2(A))
print(test.solve3(A))
print(test.solve4(A))
