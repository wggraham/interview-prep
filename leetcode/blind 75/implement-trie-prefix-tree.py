class Node:
    def __init__(self, val=False):
        self.val = val
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.val = True

    def _scan(self, word: str) -> Node:
        node = self.root
        for c in word:
            if c not in node.children:
                return
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self._scan(word)
        return node and node.val

    def startsWith(self, prefix: str) -> bool:
        node = self._scan(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
w = "apple"
p = "prefix"
obj = Trie()
obj.insert(w)
param_2 = obj.search(w)
param_3 = obj.startsWith(p)
