class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, c in enumerate(haystack):
            j = 0
            while i + j < len(haystack) and j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle):
                return i

        return -1

    def strStrKMP(self, haystack: str, needle: str) -> int:
        z = [0] * len(needle)
        j = 0
        for i, c in enumerate(needle):
            if c == needle[j]:
                z[j] = z[j-1] + 1
        


haystack = "sadbutsad"
needle = "sad"
haystack = "mississippi"
needle = "issip"
test = Solution()
print(test.strStr(haystack, needle))
