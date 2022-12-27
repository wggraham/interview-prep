from collections import deque, Counter


class Solution:
    def solve(self, A):
        counts = Counter()
        q = deque()
        res = []
        for c in A:
            if c not in counts:
                q.append(c)

            counts[c] += 1
            while q and counts[q[0]] > 1:
                q.popleft()

            res += [q[0]] if q else ['#']
        return ''.join(res)


A = "abadbc"
A = "abcabc"
test = Solution()
print(test.solve(A))
