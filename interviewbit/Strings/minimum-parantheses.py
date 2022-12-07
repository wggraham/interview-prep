class Solution:
    def solve(self, A):
        oCount, cCount, res = 0, 0, 0
        for p in A:
            oCount += 1 if p == '(' else 0
            cCount += 1 if p == ')' else 0
            if cCount > oCount:
                res += 1
                oCount, cCount = 0, 0
        return res + abs(oCount - cCount)

a = "))(("
test = Solution()
print(test.solve(a))
