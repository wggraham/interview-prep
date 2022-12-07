class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        if not A: return []
        res = []

        def getParen(n, oCount, cCount, combo):
            if not n:
                res.append(''.join(combo))
                return
            if oCount < A:
                getParen(n - 1, oCount + 1, cCount, combo + ['('])
            if oCount > cCount:
                getParen(n - 1, oCount, cCount + 1, combo + [')'])

        getParen(2 * A, 0, 0, [])
        return res


n = 3
test = Solution()
print(test.generateParenthesis(n))
