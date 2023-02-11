from collections import deque


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0] = [i for i in range(m + 1)]
        for i in range(n + 1):
            dp[i][0] = i

        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                if c1 == c2 and dp[i - 1][j - 1] < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

    def minDistance2(self, word1: str, word2: str) -> int:
        q, res, seen, n, m = deque([(0, 0)]), 0, set(), len(word1), len(word2)
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                while i < n and j < m and word1[i] == word2[j]:
                    i, j = i + 1, j + 1

                if i == n and j == m:
                    return res

                for ind in [(i, j + 1), (i + 1, j + 1), (i + 1, j)]:    # insert, edit, delete
                    if ind not in seen:
                        seen.add(ind)
                        q.append(ind)
            res += 1


# word1 = "horse"
# word2 = "ros"
word1 = "intention"
word2 = "execution"
# word1 ="zoologicoarchaeologist"
# word2 ="zoogeologist"

test = Solution()
print(test.minDistance(word1, word2))
print(test.minDistance2(word1, word2))
