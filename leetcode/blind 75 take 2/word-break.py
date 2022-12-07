from typing import List


class Node:
    def __init__(self, end=False):
        self.end = end
        self.children = {}


class Solution:
    def __build_tree__(self, words):
        root = Node()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.end = True
        return root

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = self.__build_tree__(wordDict)
        seen, stack, n = {0}, [0], len(s)

        while stack:
            i = stack.pop()
            node = root

            while i < n and s[i] in node.children:
                node = node.children[s[i]]
                if node.end and i + 1 not in seen:
                    seen.add(i + 1)
                    stack.append(i + 1)
                i += 1
            if i == n and node.end:
                return True
        return False


s = "applepenapple"
wordDict = ["apple", "pen"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "aaaaaaa"
# wordDict = ["aaaa", "aa"]

test = Solution()
print(test.wordBreak(s, wordDict))
