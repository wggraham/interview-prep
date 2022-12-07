from collections import defaultdict


class Solution:
    def anagrams(self, words):
        ana = defaultdict(list)
        for i, word in enumerate(words):
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            ana[(*counts,)].append(i + 1)
        return list(ana.values())


words = ['cat', 'dog', 'god', 'tca']
words = ['b']
test = Solution()
print(test.anagrams(words))
