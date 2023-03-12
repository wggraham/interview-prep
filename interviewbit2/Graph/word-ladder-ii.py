import string
from collections import defaultdict, deque
from sys import maxsize
from time import time

from collections import deque
from sys import maxsize


class Node:
    def __init__(self, word="", hop=0, parent=None):
        self.word = word
        self.hop = hop
        self.parent = parent


class Solution2:
    def __getSeq__(self, node):
        res = []
        while node:
            res.append(node.word)
            node = node.parent
        return res

    def solve(self, start, end, words):
        if start == end:
            return [[start]]

        res, steps, words, q = [], maxsize, set(words + [end]), deque([Node(start, 1)])
        while q:
            node = q.popleft()
            if node.hop > steps:
                break
            if node.word == end:
                steps = node.hop
                res.append(self.__getSeq__(node))
                continue

            for i in range(len(node.word)):
                for c in string.ascii_lowercase:
                    word = node.word[:i] + c + node.word[i + 1:]
                    if word in words:
                        q.append(Node(word, node.hop + 1, node))
                        if word != end:
                            words.remove(word)
        return res


class Solution:
    def findLadders(self, start, end, dictV):
        if start == end:
            return [start]

        def is_adj(w1, w2):
            n, delta = len(w1), 0
            for i in range(n):
                if w1[i] != w2[i]:
                    delta += 1
                if delta > 1:
                    return False
            return True

        adj_map = defaultdict(set)
        all_words = [start] + [end] + dictV
        for word in all_words:
            for w in all_words:
                if w == word: continue
                if is_adj(word, w):
                    adj_map[word].add(w)

        q = deque([(start, set(dictV + [end]), [start], 0)])
        found_step = maxsize
        res = []
        while q:
            word, words, seq, step = q.popleft()
            if step > found_step:
                return res
            if word == end:
                found_step = step
                res.append(seq)
                continue
            q.extend([(w, words.difference(w), seq + [w], step + 1) for w in adj_map[word]])

        return res

    def findLadders2(self, start, end, words):
        words, q, visited, steps, seq = set(words + [end]), deque([(start, 1, [start])]), set(), maxsize, []
        while q:
            word, step, ladder = q.popleft()
            visited.add(word)
            if step > steps:
                break
            if word == end:
                steps = step
                seq.append(ladder)

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in words and new_word not in visited:
                        q.append((new_word, step + 1, ladder + [new_word]))
        return seq


start = "hit"
end = "cog"
d = ["hot", "dot", "dog", "lot", "log"]
start = "abbbbbaabbaabaaabbaabababbbabaabaababbababbaaa"
end = "babaaaababaaaabababbabbbabbbbaababbbbbaabbbbaa"
d = ["babbabbaaabaabaaabbaaabaaaabaaaaabbabbabbababa", "baaaabaabbaabaaabbbaabbaabbbabbaabbabbbbbaaaab",
     "aabaabaabaaabaababbabbaaabaaabbababbaaabbaaaab", "babbbaaaaabbabaabbabaaaaabbbbbbaabbbaabaabbabb",
     "abbaaabaabaababbabbbbabbbaaaaababbbabbaabbaaab", "bbaabbbaaabbababaabaaaaaaaaaaabaabaaaaaababaab",
     "abbaaaaaabbbaabbabbabaaabbbbbabababababababbba", "baaaaaaaabbaabbaaaabbbbabbbababaaabaaaabbbbaba",
     "abbabbbbaabababaabbaaaabbbbbbababbaabababaaaab", "abbaaaaaabaaaaaababbabbbbbaaabbbabbaaaababaaba",
     "baabbbbbbbbbbababaabbbbbaabaababaaaababbabbbba", "baaaaaaabbaaaabbabaabaabbbaababaabbbaababbabba",
     "aababaabaaabbaabaabbababababaaaabaaaaaabbaabaa", "abababaabbabaaabbabbabbabaaaabbbbbabaaabbaabba"]
start = "aabbaaba"
end = "aababaaa"
d = ["baabbaaa", "baabbbab", "bbbabbaa", "bbabbaba", "abbaabaa", "aabbbabb", "abababbb", "abaaabba", "bbbaaabb",
     "abbaaaab", "abababab", "abbbabab", "abaaaabb", "aaaaabaa", "baaaabaa", "bbabbabb", "ababaaab", "aabaabab",
     "babbbaba", "bbbaaabb", "babaaabb", "aabaaaab", "bbaabbaa", "aaababaa", "bbbbabab", "aaaababa", "bbbbbaba",
     "abaabaab", "baaababb", "bbabbaaa", "abbbbbab", "bbbbbabb", "abaaabaa", "babbaabb", "babaabab", "aabbbbba",
     "baabaabb", "ababbabb", "aababaab"]

test = Solution()
test2 = Solution2()
t0 = time()
print(test.findLadders(start, end, d))
t1 = time()
print(test.findLadders2(start, end, d))
t2 = time()
print(test.findLadders(start, end, d))
t3 = time()
print(t1 - t0)
print(t2 - t1)
print(t3 - t2)
