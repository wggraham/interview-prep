from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount, sCount, res, j = Counter(p), Counter(), [], 0

        for i, c in enumerate(s):
            if c not in pCount:
                j = i + 1
                sCount = Counter()
                continue

            while sCount[c] == pCount[c]:
                sCount[s[j]] -= 1
                j += 1

            sCount[c] += 1
            if i - j + 1 == len(p):
                res.append(j)
                sCount[s[j]] -= 1
                j += 1

        return res


s = "cbaebabacd"
p = "abc"
s = "abab"; p = "ab"
test = Solution()
print(test.findAnagrams(s, p))
