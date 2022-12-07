from collections import defaultdict


class Trie:
    ALPHABET_SIZE = 26

    def __init__(self):
        self.child = [None] * Trie.ALPHABET_SIZE
        self.value = 0

    @staticmethod
    def __to_index__(c):
        return ord(c) - ord('a')

    def add_word(self, j, word):
        trie = self
        for c in reversed(word):
            idx = Trie.__to_index__(c)
            trie.child[idx] = trie = Trie()
        trie.value = j


def make_trie(words):
    trie = Trie()

    for i, word in enumerate(words):
        trie.add_word(i, word)

    return trie


class PalindromePairs:
    @staticmethod
    def __is_palindrome__(word):
        return word == word[::-1]

    @staticmethod
    def find_pairs(words):
        trie = make_trie(words)


        for i, word in enumerate(words):
            for c in word:






w = ["abcd", "dcba", "lls", "s", "sssll"]
print(PalindromePairs.find_pairs(w))
