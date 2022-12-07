from collections import Counter
from sys import maxsize

class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t): return ''
        if s == t: return t

        indices, shortest, window_counts, j, total, counts_t = (None, None), maxsize, Counter(), 0, len(t), Counter(t)
        for i, c in enumerate(s):
            if c not in counts_t: continue

            window_counts[c] += 1
            total -= 1 if window_counts[c] <= counts_t[c] else 0

            if not total:
                while s[j] not in counts_t or window_counts[s[j]] > counts_t[s[j]]:
                    window_counts[s[j]] -= 1
                    j += 1
                if i - j + 1 < shortest:
                    shortest = i - j + 1
                    indices = (j, i)

        return s[indices[0]:indices[1] + 1] if indices[0] is not None else ''


A = "AAAAAA"
B = "AA"
test = Solution()
print(test.minWindow(A, B))
