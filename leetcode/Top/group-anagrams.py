import string
from collections import defaultdict, Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words, res = defaultdict(list), []
        for i in range(len(strs)):
            words[''.join(sorted(list(strs[i])))].append(i)

        for _, indices in sorted(words.items()):
            res.extend([[strs[i] for i in indices]])
        return res

    def groupAnagramsCounts(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            counts = Counter(word)
            key = tuple([v for c in string.ascii_lowercase for v in (c, counts[c]) if c in counts])
            res[key].append(word)
        return [lst for lst in res.values()]

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    def groupAnagramsCounts2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            counts = Counter(word)
            key = *(v for c in string.ascii_lowercase for v in (c, counts[c]) if c in counts),
            res[key].append(word)
        return [lst for lst in res.values()]


strs = ["eat","tea","tan","ate","nat","bat"]
test = Solution()
print(test.groupAnagrams(strs))
print(test.groupAnagramsCounts(strs))
print(test.groupAnagramsCounts2(strs))
