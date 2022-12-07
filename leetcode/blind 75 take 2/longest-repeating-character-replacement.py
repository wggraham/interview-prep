from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter(s[:max(1,k)])
        maxCount, n = 0, len(s)
        s += '.'
        i, j = max(1,k), 0
        while i < len(s):
            while i < len(s) and (i - j + 1) <= (count.most_common(1)[0][1] + k):    # grow right until k changes done
                count[s[i]] += 1
                i += 1
            maxCount = max(maxCount, min(n, count.most_common(1)[0][1] + k))

            while j < i < len(s) and (i - j + 1) > (count.most_common(1)[0][1] + k):
                count[s[j]] -= 1
                j += 1

        return maxCount

    # this approach takes advantage of the fact that you don't need to return the
    # actual substring.  Therefore, you don't have to track what the current most
    # common character is while iterating.  You can simply track what the largest
    # set of common characters that occurs within a range where at most K changes
    # have occurred.  You are shrinking the left side of sliding window if it ever
    # gets larger than (max(most_common_count + k))
    def characterReplacement2(self, s: str, k: int) -> int:
        commonCount, maxLen, j, count = 0, 0, 0, Counter()

        for i, c in enumerate(s):
            count[c] += 1
            commonCount = max(commonCount, count[c])

            if i - j + 1 - commonCount > k:
                count[s[j]] -= 1
                j += 1
            maxLen = max(maxLen, i - j + 1)
        return maxLen



s = "AABA";
k = 0
s = "AABABBA";
k = 1
# s = "ABAA";
# k = 0
s = "ABAB"
k = 2
test = Solution()
print(test.characterReplacement2(s, k))
