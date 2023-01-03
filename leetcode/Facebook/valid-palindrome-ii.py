class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j, skips, k, o = 0, len(s) - 1, 0, 0, 0
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
                continue

            skips += 1
            if skips == 2:
                break
            k, o = i, j
            j -= 1

        if skips < 2:
            return True

        i, j, skips = k, o, 0
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
                continue

            skips += 1
            if skips == 2:
                break
            i += 1

        return skips < 2


s = "abc"
# s = "deeee"
test = Solution()
print(test.validPalindrome(s))