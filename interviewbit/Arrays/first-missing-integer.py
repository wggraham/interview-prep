class Solution:
    def firstMissingPositive(self, A):
        contains = set([x for x in A if x > 0])

        for i in range(1, len(A) + 1):
            if i not in contains:
                return i


a = [ 1 ]

test = Solution()
print(test.firstMissingPositive(a))
