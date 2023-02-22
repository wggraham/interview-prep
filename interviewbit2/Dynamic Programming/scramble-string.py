from collections import defaultdict
from functools import lru_cache


class Solution:
    def isScramble(self, A, B):
        if len(A) != len(B): return 0

        @lru_cache(None)
        def try_all(a, b):
            if not a and not b: return True
            if not a or not b: return False
            if len(a) != len(b): return False
            if set(a) != set(b): return False
            if a == b: return True

            m = len(a) // 2
            res = try_all(a[:m], b[:m]) and try_all(a[m:], b[m:])
            res |= try_all(a[:m], b[m - 1:]) and try_all(a[m:], b[:m - 1])
            res = try_all(a[:m - 1], b[:m - 1]) and try_all(a[m - 1:], b[m - 1:])
            res |= try_all(a[:m], b[m - 1:]) and try_all(a[m:], b[:m - 1])
            res |= try_all(a[:m - 1], b[m:]) and try_all(a[m - 1:], b[:m])
            res |= try_all(a[:m], b[m:]) and try_all(a[m:], b[:m])
            return (try_all(a[:m], b[:m]) and try_all(a[m:], b[m:])) or res

        return 1 if try_all(A, B) else 0

    def isScramble2(self, A, B):
        if len(A) != len(B): return 0

        @lru_cache(None)
        def try_all(a, b):
            if not a and not b: return True
            if (not a and b) or (not b and a): return False
            if len(a) < 4:
                return sorted(a) == sorted(b)
            m = len(a) // 2
            a_1, a_2 = a[:m], a[m:]
            a_11, a_22 = a[:m - 1], a[m - 1:]
            b_1, b_2 = b[:m], b[m:]
            b_11, b_22 = b[:m - 1], b[m - 1:]

            sorted_a1 = sorted(a_1)
            sorted_a2 = sorted(a_2)
            sorted_a11 = sorted(a_11)
            sorted_b1 = sorted(b_1)
            sorted_b2 = sorted(b_2)
            sorted_b11 = sorted(b_11)
            sorted_b22 = sorted(b_22)

            found = False
            if sorted_a1 == sorted_b1:
                found = try_all(a_1, b_1) and try_all(a_2, b_2)
            elif sorted_a1 == sorted_b22:
                found = try_all(a_1, b_22) and try_all(a_2, b_11)
            elif sorted_a11 == sorted_b11:
                found = try_all(a_11, b_11) and try_all(a_22, b_22)
            elif sorted_a11 == sorted_b1:
                found = try_all(a_11, b_1) and try_all(a_22, b_2)
            return found

        return int(try_all(A, B))

    def isScramble3(self, A, B):
        @lru_cache(None)
        def explore(i, j, l):
            if l == 1:
                return A[i] == B[j]

            for k in range(1, l):
                if (explore(i, j, k) and explore(i + k, j + k, l - k)) or \
                        (explore(i, j + l - k, k) and explore(i + k, j, l - k)):
                    return True

            return False

        return int(explore(0, 0, len(A)))

    def isScramble4(self, A, B):
        def explore(i, j, l):
            key = (i, j, l)
            if key in dp:
                return dp[key]
            if l == 1:
                dp[key] = A[i] == B[j]
                return dp[key]

            for k in range(1, l):
                if (explore(i, j, k) and explore(i + k, j + k, l - k)) or \
                        (explore(i, j + l - k, k) and explore(i + k, j, l - k)):
                    dp[key] = True
                    return True

            return dp[key]

        dp = defaultdict(bool)
        return int(explore(0, 0, len(A)))


a = "great"
b = "rgtae"
A = "abbbcbaaccacaacc"
B = "acaaaccabcabcbcb"
test = Solution()
print(test.isScramble2(A, B))
print(test.isScramble3(A, B))
