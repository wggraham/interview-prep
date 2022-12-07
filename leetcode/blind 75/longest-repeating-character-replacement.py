from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count, max_len = 0, 0
        counts = Counter()

        for i, c in enumerate(s):
            counts[c] += 1                          # add next char to char counts (increment right side of window)
            max_count = max(max_count, counts[c])   # update max char count in window
            if max_len < k + max_count:             # check if longest seq seen thus far is < max char count in window + wildcard count
                max_len += 1                        # increment longest seq seen if wildcard # + char count >
                continue

            counts[s[i-max_len]] -= 1               # pop left side of window when its length >= longest char count + wildcard

        return max_len

