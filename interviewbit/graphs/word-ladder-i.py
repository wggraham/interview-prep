from collections import deque


class Solution:
    def solve(self, A, B, C):
        if A == B: return 1
        d = set(C + [B])

        q = deque([(A, 1)])
        while q:
            word, hop = q.popleft()
            if word == B:
                return hop
            # get adjacent words by replacing each character with all possible
            for i in range(len(word)):
                for j in range(27):
                    c = chr(ord('a') + j)
                    s = word[:i] + c + word[i + 1:]
                    if s in d:
                        q.append((s, hop + 1))
                        d.remove(s)
        return 0


A = "hit"
B = "cog"
C = ["hot", "dot", "dog", "lot", "log"]

test = Solution()
print(test.solve(A, B, C))
