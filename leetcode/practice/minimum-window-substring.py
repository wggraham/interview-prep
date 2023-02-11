from collections import Counter
from sys import maxsize


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed, have, j, total, window, f, b = Counter(t), Counter(), 0, len(t), maxsize, 0, -1

        for i, c in enumerate(s):
            if c in needed:
                have[c] += 1
                if have[c] <= needed[c]:
                    total -= 1

            while j < i and s[j] not in needed or have[s[j]] > needed[s[j]]:
                j += 1
                if s[j - 1] in needed:
                    have[s[j - 1]] -= 1

            if total == 0 and i - j + 1 < window:
                window = i - j + 1
                f, b = j, i

        return s[f:b + 1]


s = "ADOBECODEBANC"
t = "ABC"
# s = "a"
# t = "a"
# s = "a"
# t = "aa"
s = "a"
t = "b"
test = Solution()
print(test.minWindow(s, t))
