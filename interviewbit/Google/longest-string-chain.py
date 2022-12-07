from sys import maxsize
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def canAdd(s, l):
            i = 0
            diff = 1
            for c in l:
                if c == s[i]:
                    i += 1
                    if i == len(s): break
                    continue
                diff -= 1
                if diff < 0:
                    return False
            return True

        minSize, maxSize = maxsize, 0
        for w in words:
            minSize = min(minSize, len(w))
            maxSize = max(maxSize, len(w))

        sizedWords = [[] for _ in range(maxSize - minSize + 1)]
        for w in words:
            sizedWords[len(w)-minSize].append(w)

        chains = {w: 1 for w in sizedWords[0]}
        longest = 1
        for words in sizedWords[1:]:
            temp = {}
            for word in words:
                for w, s in chains.items():
                    if not canAdd(w, word):
                        continue
                    temp[word] = max(temp[word], s + 1) if word in temp else s + 1
                    longest = max(longest, temp[word])
                if word not in temp:
                    temp[word] = 1
            chains = temp
        return longest


words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words =["abcd","dbqca"]
words = ["a","b","ab","bac"]
test = Solution()
print(test.longestStrChain(words))
