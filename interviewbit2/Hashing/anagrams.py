from collections import defaultdict


class Solution:
    def anagrams(self, words):
        d = defaultdict(list)
        for i, word in enumerate(words):
            d[''.join(sorted(list(word)))].append(i + 1)

        return list(d.values())

    def anagrams2(self, words):
        d = defaultdict(list)
        for i, word in enumerate(words):
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            d[tuple(counts)].append(i + 1)

        return list(d.values())


A = ['cat', 'dog', 'god', 'tca']
test = Solution()
print(test.anagrams(A))
print(test.anagrams2(A))
