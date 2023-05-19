import string
from collections import Counter
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def check(a, b):
            if len(a) != len(b): return False
            if a == b: return True
            if Counter(a) != Counter(b): return False

            for i in range(1, len(a)):
                if check(a[:i], b[:i]) and check(a[i:], b[i:]) or check(a[:i], b[-i:]) and check(a[i:], b[:-i]):
                    return True
            return False

        return check(s1, s2)

    def isScramble2(self, s1: str, s2: str) -> bool:
        def get_counts(word):
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            return counts

        @lru_cache(None)
        def check(a, b):
            if len(a) != len(b): return False
            if a == b: return True
            if get_counts(a) != get_counts(b): return False

            for i in range(1, len(a)):
                if check(a[:i], b[:i]) and check(a[i:], b[i:]) or check(a[:i], b[-i:]) and check(a[i:], b[:-i]):
                    return True

            return False

        return check(s1, s2)

    def isScramble3(self, s1: str, s2: str) -> bool:
        def get_counts(word):
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            return counts

        @lru_cache(None)
        def check(a, b):
            if len(a) != len(b): return False
            if a == b: return True
            if get_counts(a) != get_counts(b): return False
            return any(
                check(a[:i], b[:i]) and check(a[i:], b[i:]) or check(a[:i], b[-i:]) and check(a[i:], b[:-i])
                for i in range(1, len(a)))

        return check(s1, s2)

    def isScramble4(self, s1: str, s2: str) -> bool:
        def get_counts(word):
            counts = [0] * 26
            for c in word:
                counts[alpha_idx[c]] += 1
            return counts

        @lru_cache(None)
        def check(a, b):
            if len(a) != len(b): return False
            if a == b: return True
            if get_counts(a) != get_counts(b): return False
            return any(
                check(a[:i], b[:i]) and check(a[i:], b[i:]) or check(a[:i], b[-i:]) and check(a[i:], b[:-i])
                for i in range(1, len(a)))

        alpha_idx = {c: i for i, c in enumerate(string.ascii_lowercase)}
        return check(s1, s2)


s1 = "great"
s2 = "ergat"
test = Solution()
print(test.isScramble(s1, s2))
print(test.isScramble2(s1, s2))
