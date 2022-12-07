class Solution:
    def braces(self, A):
        s, e = 0, 0
        while s < len(A) - e - 1:
            found1, s = self.opOccurred(A, s)
            found2, e = self.opOccurred(A[::-1], e)
            if not found1 and not found2:
                return 1
        return 0 if s != e or s > len(A) and e > len(A) else 1

    def opOccurred(self, s, i):
        opFound = False
        while i < len(s) and s[i] != "(" and s[i] != ")":
            opFound |= self.isOp(s[i])
            i += 1
        return opFound, i + 1

    def isOp(self, c):
        if c == '+' or c == '-' or c == '*' or c == '/':
            return True
        return False


test = Solution()
A = "((a + b))"
A = "(a + (a + b))"
A = "a+b"
print(test.braces(A))
