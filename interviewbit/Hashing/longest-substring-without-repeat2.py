from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, A):
        counts, longest, j = Counter(), 0, 0

        for i, c in enumerate(A):
            counts[c] += 1
            while counts[c] > 1:
                counts[A[j]] -= 1
                j += 1
            longest = max(longest, i - j + 1)

        return longest

A = "abcabcbb"
test = Solution()
print(test.lengthOfLongestSubstring(A))
