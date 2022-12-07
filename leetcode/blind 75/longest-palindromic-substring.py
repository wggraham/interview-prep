import string


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return

        digits = set(string.digits)
        alpha = set(string.ascii_lowercase)
        s = s.lower()

        def hash(s):
            nonlocal digits, alpha
            if not s: return 0

            total = 0
            for c in s:
                total *= 36
                if c in digits:
                    total += ord(c) - 47
                if c in alpha:
                    total += ord(c) - 96
            return total

        def popLeft(s, c, total):
            nonlocal digits, alpha
            v = 0
            if c in digits:
                v = ord(c) - 47
            if c in alpha:
                v = ord(c) - 96
            return total - (v*36**len(s))

        def appendRight(c, total):
            total *= 36
            v = ord(c) - 47 if c in digits else ord(c) - 96
            return total + v

        left, right = 0, 0
        lp = 1
        for k in range(1, len(s)):
            i, j = k-1, k
            while i >= 0 and j < len(s):
                left = appendRight(s[i], left)
                right = appendRight(s[j], right)
                if left > 0 and right > 0 and left != right:



s = "babad"