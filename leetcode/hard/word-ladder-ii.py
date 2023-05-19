from collections import deque
from sys import maxsize
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def is_adjacent(w1, w2):
            count = 0
            for i in range(len(w1)):
                count += w1[i] != w2[i]
                if count > 1:
                    return False
            return count == 1

        def get_adjacent_words(word, word_list):
            return {w for w in word_list if is_adjacent(word, w)}

        res, found_len, q = [], maxsize, deque([[beginWord]])
        while q:
            words = q.popleft()

            if endWord in words:
                if len(words) > found_len:
                    break
                found_len = len(words)
                res.append(words)

            q.extend([words + [word] for word in get_adjacent_words(words[-1], wordList).difference(set(words))])

        return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
test = Solution()
print(test.findLadders(beginWord, endWord, wordList))
