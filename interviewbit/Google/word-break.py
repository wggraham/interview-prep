class Trie:
    def __init__(self, isEnd = False):
        self.isEnd = isEnd
        self.children = {}

class Solution:
    def __build_trie__(self, dictionary):
        root = Trie()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.isEnd = True
        return root

    def wordBreak(self, word, dictionary):
        trie = self.__build_trie__(dictionary)
        n = len(word)

        def explore(i, node):
            nonlocal word, n, trie

            res = False
            for j, c in enumerate(word[i:], i):
                if c not in node.children: return res
                node = node.children[c]

                if node.isEnd:
                    if j == (n - 1): return True
                    res |= explore(j+1, trie)

            return res

        return explore(0, trie)

    def wordBreakIterative(self, word, dictionary):
        trie = self.__build_trie__(dictionary)
        n = len(word)

        s = [(0, trie)]
        while s:
            i, node = s.pop()

            for j, c in enumerate(word[i:], i):
                if c not in node.children: break
                node = node.children[c]

                if node.isEnd:
                    if j == (n - 1): return True
                    s.append((j + 1, trie))


A = "myinterviewtrainer"
B = ["trainer", "my", "interview"]
test = Solution()
print(test.wordBreak(A, B))
print(test.wordBreakIterative(A, B))

