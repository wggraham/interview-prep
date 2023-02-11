from collections import Counter, deque
from time import time


class Solution:
    def subsets(self, A):
        A.sort()
        n, res = len(A), []

        def gen_subsets(pre, i):
            res.append(pre)
            if i == n: return
            prev = None
            for j, v in enumerate(A[i:], i):
                if v == prev: continue
                prev = v
                gen_subsets(pre + [v], j + 1)

        gen_subsets([], 0)
        return res

    def subsets2(self, A):
        counts = sorted(list(Counter(A).items()))
        n, res = len(counts), []

        def gen_subsets(pre, i):
            res.append(pre)
            if i == n: return
            for j in range(i, n):
                for count in range(1, counts[j][1] + 1):
                    gen_subsets(pre + [counts[j][0]] * count, j + 1)

        gen_subsets([], 0)
        return res

    def subsets3(self, A):
        A.sort()
        n, res = len(A), []

        def gen_subsets(pre, i):
            res.append(pre)
            if i == n: return
            while i < n:
                j = i
                while i < n and A[i] == A[j]:
                    i += 1

                for count in range(1, i - j + 1):
                    gen_subsets(pre + [A[j]] * count, i)

        gen_subsets([], 0)
        return res

    def subsets4(self, A):
        counts = sorted(list(Counter(A).items()))
        n, res = len(counts), []
        s = [([], 0)]

        while s:
            pre, i = s.pop()
            res.append(pre)
            if i == n: continue
            for j in range(i, n):
                for count in range(1, counts[j][1] + 1):
                    s.append((pre + [counts[j][0]] * count, j + 1))

        return res

    def subsets5(self, A):
        counts = sorted(list(Counter(A).items()))
        n, res = len(counts), []
        q = deque([([], 0)])

        while q:
            pre, i = q.popleft()
            res.append(pre)
            if i == n: continue
            for j in range(i, n):
                for count in range(1, counts[j][1] + 1):
                    q.append((pre + [counts[j][0]] * count, j + 1))

        return res


A = [1, 1, 1, 2, 7,7,7,7, 2, 2, 3, 3, 3]
# A = [1,1, 2,3]
test = Solution()
t0 = time()
print(test.subsets(A))
t1 = time()
print(test.subsets2(A))
t2 = time()
print(test.subsets3(A))
t3 = time()
print(test.subsets4(A))
t4 = time()
print(test.subsets5(A))
t5 = time()
print(t1 - t0)
print(t2 - t1)
print(t3 - t2)
print(t4 - t3)
print(t5 - t4)
