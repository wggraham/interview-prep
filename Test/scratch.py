# count number of simultaneous words given a word and a stream of characters
# characters need to be in the same order as the given word, but not necessarily consecutive
from collections import defaultdict
from sys import maxsize


# what would you do if the word you must match had duplicate characters ?

class Solution:
    def simultaneous_chat_count(self, char_stream, word):
        def get_count(i, j, count):
            if j == m:
                count -= 1
                if i == n:
                    return count
                else:
                    j = 0
            if i >= n:
                return maxsize

            if dp[i][j] != maxsize:
                return dp[i][j]

            while i < n and char_stream[i] != word[j]:
                i += 1
            if i >= n:
                return maxsize
            if j == 0 and char_stream[i] == word[j]:
                count += 1
                dp[i][j] = get_count(i + 1, j + 1, count)
            else:
                dp[i][j] = min(get_count(i + 1, j + 1, count), get_count(i + 1, j, count))
            return dp[i][j]

        ans, n, m = 0, len(char_stream), len(word)
        dp = [[maxsize] * m for _ in range(n)]
        return get_count(0, 0, 1)

    def simultaneous_chat_count2(self, char_stream, word):
        n, m = len(char_stream), len(word)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0] = [i for i in range(m + 1)]
        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            dp[i][1] += 1 if char_stream[i-1] == word[0] else 0
            for j in range(1, m + 1):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                # dp[i][j] = dp[i-1][j-1] if char_stream[i-1] == word[j-1] else dp[i][j]

        return dp[-1][-1]

    def simultaneous_chat_count3(self, char_stream, word):
        letters, char_pos_map = {c for c in word}, defaultdict(list)

        for i, c in enumerate(char_stream):
            char_pos_map[c].append(i)

        count = n = len(char_pos_map[word[0]])
        for c, indices in char_pos_map.items():
            if c not in letters or len(indices) != n:
                return -1

        for i in range(n):
            prev_idx = char_pos_map[word[-1]].pop()

            for c in reversed(word[:-1]):
                idx = char_pos_map[c].pop()
                if idx >= prev_idx:
                    return -1
                prev_idx = idx

            if char_pos_map[word[-1]] and prev_idx > char_pos_map[word[-1]][-1]:
                count -= 1

        return count

    def simultaneous_chat_count4(self, char_stream, word):
        dp = defaultdict(bool)
        n, m = len(char_stream), len(word)
        res = 0

        def explore(i, j, count):
            nonlocal res
            if i > n or j > m:
                return False
            if (i, j, count) in dp:
                return dp[(i, j, count)]
            if j == 0:
                count += 1 if i < n and char_stream[i] == word[0] else 0
            if j == m:
                count -= 1
                if i == n:
                    return count == 0
                j = 0
            if i == n:
                return False
            if char_stream[i] == word[j]:
                dp[(i, j, count)] = explore(i + 1, j + 1, count)
            dp[(i, j, count)] |= explore(i + 1, j, count)

            if dp[(i, j, count)]:
                res = max(res, count)
            return dp[(i, j, count)]
        explore(0, 0, 0)
        return res

s = "cchhcchathataattchat"
s = "chcchchh"
word = 'chch'
test = Solution()
print(test.simultaneous_chat_count(s, word))
print(test.simultaneous_chat_count2(s, word))
# print(test.simultaneous_chat_count3(s, word))
print(test.simultaneous_chat_count4(s, word))
