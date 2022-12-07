from collections import defaultdict


class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = defaultdict()


class Solution:
    def wordBreak(self, A, B):

        def buildTrie():
            nonlocal B
            root = Trie()
            for word in B:
                node = root
                for i, c in enumerate(word):
                    if c not in node.children:
                        node.children[c] = Trie()
                    node = node.children[c]
                    if i == (len(word) - 1):
                        node.val = word
            return root

        def getSentence(s, node, p):
            nonlocal root
            nonlocal res
            if not s:
                res.append(p)
                return
            for i, c in enumerate(s):
                if c not in node.children:
                    return
                node = node.children[c]
                if node.val:
                    getSentence(s[i + 1:], root, p + [node.val])
            return res

        def convertToStrings(l):
            for i in range(len(l)):
                l[i] = ' '.join(l[i])

        res = []
        root = buildTrie()
        getSentence(list(A), root, [])
        convertToStrings(res)
        res.sort()
        return res


A = "catsanddog"
B = ["cat", "cats", "and", "sand", "dog"]
test = Solution()
print(test.wordBreak(A, B))
