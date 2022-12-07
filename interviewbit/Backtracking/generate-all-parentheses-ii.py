class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):

        def genP(lcount, rcount, part):
            p = []
            if not lcount and not rcount:
                return [''.join(part)]
            if lcount:
                p += genP(lcount - 1, rcount, part + ['('])
            if rcount > lcount:
                p += genP(lcount, rcount - 1, part + [')'])
            return p

        return genP(A, A, [])


n = 3
test = Solution()
print(test.generateParenthesis(n))
