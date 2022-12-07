class Trie:
    def __init__(self, end=False):
        self.end = end
        self.child = {}


def build_trie(words):
    root = Trie()
    for word in words:
        node = root
        for c in word:
            if c not in node.child:
                node.child[c] = Trie()
            node = node.child[c]
        node.end = True
    return root


class Solution:
    def wordBreak(self, A, B):
        if not A or not B:
            return 0

        def can_reach_end():
            visited = set()
            indices = {0}
            while len(A[0]) not in indices and len(indices) > 0:
                visited = visited.union(indices)
                indices = get_next_indices(indices).difference(visited)

            return len(A[0]) in indices

        def get_next_indices(indices):
            end_indices = set()
            for i in indices:
                node = trie
                while i < len(A[0]) and A[0][i] in node.child:
                    node = node.child[A[0][i]]
                    i += 1
                    if node.end:
                        end_indices.add(i)

            return end_indices

        trie = build_trie(B)
        return 1 if can_reach_end() else 0


A = "myinterviewtrainer",
B = ["trainer", "my", "interview"]
test = Solution()
print(test.wordBreak(A, B))
