from collections import deque
from typing import List


class Node:
    def __init__(self, end=False):
        self.end = end
        self.children = [None] * 26


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def build_trie(words):
            root = Node()
            for word in words:
                node = root
                for c in word:
                    if not node.children[ord(c) - ord('a')]:
                        node.children[ord(c) - ord('a')] = Node()
                    node = node.children[ord(c) - ord('a')]
                node.end = True
            return root

        q, root, n, res = deque([(0, [])]), build_trie(wordDict), len(s), []
        while q:
            i, words = q.popleft()
            if i == n:
                res.append(words)
                continue
            node = root
            for j in range(i, n):
                node = node.children[ord(s[j]) - ord('a')]
                if not node:
                    break
                if node.end:
                    q.append((j + 1, words + [s[i:j+1]]))
        return [' '.join(word for word in sentence) for sentence in res]


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
test = Solution()
print(test.wordBreak(s, wordDict))
