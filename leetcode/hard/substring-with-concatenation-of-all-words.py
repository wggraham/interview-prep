from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        total, res, n, m, counts, f_counts, visited, i = 0, [], len(words), len(words[0]), Counter(
            words), Counter(), set(), 0
        while i <= len(s) - n * m:
            f_counts, total = Counter(), 0
            for j in range(i, len(s), m):
                word = s[j:j + m]
                if word not in counts or j in visited:
                    i = j
                    break

                k = max(0, j - n * m)
                visited.add(j)
                while f_counts[word] >= counts[word]:
                    f_counts[s[k:k + m]] -= 1
                    k += m
                    total -= 1

                f_counts[word] += 1
                total += 1
                if total == n:
                    res.append(j + m - n * m)
            i += 1
        return res

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        total, res, n, m, counts, f_counts = 0, [], len(words), len(words[0]), Counter(words), Counter()
        for i in range(0, len(s), m):
            word = s[i:i + m]
            if word not in counts:
                f_counts, total = Counter(), 0
                continue

            j = i - n * m
            while j >= 0 and (f_counts[word] >= counts[word] or total > n):
                f_counts[s[j:j + m]], j, total = f_counts[s[j:j + m]] - 1, j + m, total - 1

            f_counts[word], total = f_counts[word] + 1, total + 1
            res += [i + m - n * m] if total == n else []

        return res

    def findSubstring3(self, s: str, words: List[str]) -> List[int]:
        res, n, m = [], len(words), len(words[0])
        for i in range(m):
            k, counts = i, Counter(words)
            for j in range(k, len(s) + 1 - m, m):
                word = s[j: j + m]
                counts[word] -= 1

                while counts[word] < 0:
                    counts[s[k: k + m]] += 1
                    k += m
                res += [k] if k + n * m == j + m else []

        return res

    def find_chars(self, s: str, chars: List[str]) -> List[int]:
        counts, n = Counter(chars), len(chars)
        i_counts = Counter()
        total = 0
        res = []
        for i, c in enumerate(s):
            if c not in counts:
                i_counts = Counter()
                total = 0
                continue
            j = i - n
            while c in counts and i_counts[c] == counts[c]:
                i_counts[chars[j]] -= 1
                j += 1
                total -= 1
            i_counts[c] += 1
            total += 1

            if total == n:
                res.append(i - n + 1)
        return res


s = "barfoothefoobarman"
# chars = ['f', 'o', 'o']
words = ["foo", "bar"]
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo", "barr", "wing", "ding", "wing"]
s = "foobarfoobar"
words = ["foo", "bar"]
s = "a"
words = ["a"]
s = "aaaaaaaaaaaaaa"
words = ["aa","aa"]
s = "dddddddddddd"
words = ["dddd","dddd"]
test = Solution()
# print(test.find_chars(s, chars))
print(test.findSubstring(s, words))
print(test.findSubstring3(s, words))
# print(test.findSubstring2(s, words))
