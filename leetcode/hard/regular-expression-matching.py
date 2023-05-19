from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache
        def is_match(i, j):
            if j == m:
                return i == n

            found = False
            if p[j] == '.' or p[j] == s[i]:
                return is_match(i + 1, j + 1)
            elif p[j] == '*':
                if j == 0:
                    return True
                if p[j - 1] == '.':
                    while 0 < i < n:
                        found |= is_match(i + 1, j + 1)
                        i += 1
                else:
                    found |= is_match(i, j + 1)
                    while 0 < i < n and s[i] == p[j - 1]:
                        found |= is_match(i + 1, j + 1)
                        i += 1

            return found

        n, m = len(s), len(p)
        return is_match(0, 0)

    def isMatch2(self, s: str, p: str) -> bool:
        @lru_cache
        def is_match(i, j):
            if j == -1:
                return i == -1
            found = False
            if p[j] == '.' or (i >= 0 and p[j] == s[i]):
                return is_match(i - 1, j - 1)
            elif p[j] == '*':
                found |= is_match(i, j - 2)
                while i >= 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):
                    found |= is_match(i-1, j - 2)
                    i -= 1
            return found

        return is_match(len(s) - 1, len(p) - 1)


s = "aa"
p = "a"
p = "a*"
s = "ab"
p = ".*"
# s = "aab"
# p = "c*a*b"
test = Solution()
print(test.isMatch(s, p))
print(test.isMatch2(s, p))
