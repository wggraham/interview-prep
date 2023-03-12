from collections import deque
from sys import maxsize


class Node:
    def __init__(self, word="", hop=0, parent=None):
        self.word = word
        self.hop = hop
        self.parent = parent


class Solution:
    def __getSeq__(self, node):
        res = []
        while node:
            res.append(node.word)
            node = node.parent
        return res

    def solve(self, A, B, C):
        res = []
        if A == B:
            return [[A]]
        d = set(C + [B])

        sLen = maxsize
        q = deque([Node(A, 1)])
        while q:
            node = q.popleft()

            if node.hop > sLen:
                break
            if node.word == B:
                sLen = node.hop
                res.append(self.__getSeq__(node))
                continue
            # get adjacent words by replacing each character with all possible
            for i in range(len(node.word)):
                for j in range(27):
                    c = chr(ord('a') + j)
                    s = node.word[:i] + c + node.word[i + 1:]
                    if s in d:
                        q.append(Node(s, node.hop + 1, node))
                        if s != B:
                            d. remove(s)
        return res


start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]

test = Solution()
print(test.solve(start, end, dict))
