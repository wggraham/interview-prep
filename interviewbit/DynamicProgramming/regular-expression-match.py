class Solution:
    def getPostStarIndex(self, s):
        for i, c in enumerate(s):
            if c != '*':
                return i
        return len(s) if s else 0

    def cMatch(self, a, b):
        return True if b == '?' or a == b else False

    def removeRedundantStars(self, s):
        res = []
        i = 0
        while i < len(s):
            res.append(s[i])
            if s[i] == '*':
                while i < len(s) and s[i] == '*':
                    i += 1

            else:
                i += 1
        return ''.join(res)

    def isMatch(self, A, B):
        n, m = len(A), len(B)
        if not m:
            return 1 if not n else 0

        i, j = 0, 0
        inc_j = 0
        while i < n and j < m:
            inc_j = self.getPostStarIndex(B[j:])

            if self.cMatch(A[i], B[j]):
                i += 1
                j += 1
            elif not inc_j:
                return 0
            j += inc_j

        r = self.getPostStarIndex(B[j:])
        return 1 if A[n - 1 - r:] == B[m - 1 - r:] or (i == n and j + r == m) \
                    or (j + r == m and inc_j) else 0

    def isMatch2(self, A, B):

        if not len(B):
            return 1 if not len(A) else 0

        B = self.removeRedundantStars(B)
        i, j = 0, 0
        star = None
        n, m = len(A), len(B)

        while i < n:
            if j < m and self.cMatch(A[i], B[j]):
                i += 1
                j += 1
            elif j < m and B[j] == '*':
                j += 1
                star = (i, j)
            elif star:
                star = (star[0] + 1, star[1])
                i, j = star
            else:
                return 0

        return 1 if j == m or A[n - m - j:] == B[j:] else 0


A = "bbbcbcb"
B = "**cb"
# A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# B = "a**************************************************************************************"
A = "cbcacacabac"
B = "c"
# A = "acba"
# B = "*?b*a*ba*"
test = Solution()
print(test.isMatch(A, B))
print(test.isMatch2(A, B))
