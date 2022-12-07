class Node:
    def __init__(self, wordEnd=False):
        self.chars = {}
        self.end = wordEnd


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        s = [0]
        sn = {0}
        root = Node()

        def constructTree(r):
            for word in B:
                node = r
                for i, c in enumerate(word):
                    if c not in node.chars:
                        node.chars[c] = Node()
                    node = node.chars[c]

                    if i == len(word) - 1:
                        node.end = True
            return r

        def scanTree(i, tree, seen, indices):
            for j in range(i, len(A)):
                if A[j] not in tree.chars:
                    break
                tree = tree.chars[A[j]]
                if tree.end and j+1 not in seen:
                    indices.append(j+1)
                    seen.add(j+1)

        constructTree(root)
        while s:
            index = s.pop()
            if index == len(A):
                return 1
            scanTree(index, root, sn, s)
        return 0


A = "abababababaaaabaabbbabbbabbababbb"
B = [ "abbbabaa", "baabaaaab", "babaaaaaba", "b", "b", "bbaaaab", "aaabbb", "aabbbbbab", "abbb", "abaa", "aaababaab", "aabbabaa", "bab", "bbbbaabbb" ]
#A="leetcode"
#B=["leet","code"]
test = Solution()
print(test.wordBreak(A, B))
