from collections import Counter
from sys import maxsize


class Solution:
    def minWindow(self, A, B):
        total, counts = len(B), Counter(c for c in B)
        j = 0
        min_len = maxsize
        for i, c in enumerate(A + " "):
            if c in counts:
                counts[c] -= 1
                if counts[c] >= 0:
                    total -= 1

            while total == 0:
                if i - j < min_len:
                    min_len = i - j
                    rng = [j, i]
                min_len = min(min_len, i - j)
                if A[j] in counts:
                    counts[A[j]] += 1
                    if counts[A[j]] > 0:
                        total += 1
                j += 1

        return A[rng[0]:rng[1] + 1] if min_len != maxsize else ""


A = "ADOBECODEBANC"
B = "ABC"
A = "Aa91b"
B = "ab"
# A = "w"
# B = "o"
# A = "AAAAAA"
# B = "AA"
test = Solution()
print(test.minWindow(A, B))
