from collections import deque


class Solution:
    def slidingMaximum(self, A, B):
        res, q = [], deque()
        for i, v in enumerate(A):
            while q and A[q[-1]] <= v:
                q.pop()

            q.append(i)
            if A[q[0]] < i - B + 1:
                q.popleft()

            res += [A[q[0]]] if i >= B - 1 else []

        return res

    def slidingMaximum2(self, A, B):
        res, q = [], deque([A.index(max(A[:B-1]))])
        for i, v in enumerate(A[B-1:], B - 1):
            while q and A[q[-1]] <= v:
                q.pop()

            q.append(i)
            if A[q[0]] < i - B + 1:
                q.popleft()

            res.append(A[q[0]])

        return res


A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
# A = [1]
# B = 1
test = Solution()
print(test.slidingMaximum(A, B))
print(test.slidingMaximum2(A, B))
