import string
from collections import defaultdict, Counter
from copy import copy, deepcopy
from heapq import heappop, heappush


class Solution:
    def solve(self, A, B):
        a, h = list(A), []
        for i, d in enumerate(a):
            heappush(h, (-int(d), -i))

        s, count, n = [], B, len(a)
        for i in range(n):
            d = int(a[i])
            if d < -h[0][0] and count:
                heappush(h, (-d, h[0][1]))
                dd, j = heappop(h)
                a[-j] = a[i]
                s.append(str(-dd))
                count -= 1
            else:
                s.append(a[i])

        return ''.join(s)

    def solve2(self, A, B):
        a, k, n = [int(v) for v in A], B, len(A)
        digits = defaultdict(list)
        # bucket indices by digit value
        for i, c in enumerate(a):
            digits[int(c)].append(i)

        #
        res, j = [], 0
        for d in reversed(range(1, 10)):
            if d not in digits: continue

            p = []
            #
            for i in reversed(digits[d]):
                while j < n and a[j] >= d:
                    res.append(a[j])
                    j += 1

                if not k: break
                if i < j: break

                heappush(p, -a[j])
                res.append(d)
                k -= 1
                j += 1

            # replace in original string the values used with swapped values
            if not len(p): continue
            for i in digits[d][-len(p):]:
                a[i] = -heappop(p)
            if not k: break

        return ''.join([str(v) for v in res + a[len(res):]])

    # greedy doesn't work because successive swaps at the same index could benefit from
    # non locally optimized ordering (1 swap round optimized)
    # could potentially perform a second swap that results in higher value using a lower
    # value first swap value at that index

    # so you have to try all possibilities, no smart approach exists for all possible input
    # values
    def solve22(self, s, k):
        a = [int(c) for c in s]
        digits = defaultdict(list)
        for i in reversed(range(len(a))):
            digits[a[i]].append(i)

        ordered = [i for i in range(10) if i in digits]

        remaining = len(digits[ordered[-1]])
        p = []
        for i in range(len(a)):
            if not k:
                break
            if a[i] == ordered[-1]:
                digits[ordered[-1]].pop()
                remaining -= 1
            if a[i] < ordered[-1]:
                heappush(p, -a[i])
                a[i] = ordered[-1]
                remaining -= 1
                k -= 1
            if not remaining:
                for j in reversed(digits[ordered.pop()]):
                    a[j] = -heappop(p)
                    digits[a[j]].append(j)
                remaining = len(digits[ordered[-1]])
        while p:
            j = digits[ordered[-1]].pop()
            a[j] = -heappop(p)

        return ''.join(str(d) for d in a)




    def solve3(self, A, B):
        def swap(s, i, j):
            s1 = s[:i]
            s2 = s[i + 1:j]
            s3 = s[j + 1:]
            return s1 + s[j] + s2 + s[i] + s3

        def sswap(A, B, ans):
            if B == 0:
                return ans[0]
            for i in range(len(A)):
                for j in range(i + 1, len(A)):
                    if A[j] > A[i]:
                        temp = swap(A, i, j)
                        if ans[0] < temp:
                            ans[0] = temp
                        sswap(temp, B - 1, ans)

        ans = [A]
        sswap(A, B, ans)
        return ans[0]

    def solve4(self, A, B):
        def get_max(s, k, t, digits):
            if not k: return s

            largest_digit = max(d for d in range(10) if d in digits)
            if s[0] == largest_digit:
                digits[s[0]].pop()
                return [s[0]] + get_max(s[1:], k, t + 1, deepcopy(digits))

            best, res = 0, []
            for i in range(len(digits[largest_digit])):
                j = digits[largest_digit][i]
                d2 = deepcopy(digits)
                d2[largest_digit].pop(i)
                x = [s[j-t]] + get_max(s[1:j-t] + [s[0]] + s[j + 1 - t:], k - 1, t + 1, d2)
                tt = int(''.join(str(v) for v in x))
                if best < tt:
                    best = tt
                    res = x

            return res

        d = defaultdict(list)
        for i in reversed(range(len(A))):
            d[int(A[i])].append(i)
        return ''.join(str(v) for v in get_max([int(c) for c in A], B, 0, d))


    def solve5(self, A, B):

        maxm = float('-inf')

        def swap(s, i, j):
            l = list(s)
            l[i], l[j] = l[j], l[i]
            s = "".join(l)
            return s

        def helper(s, k):
            nonlocal maxm
            if int(s) > maxm:
                maxm = int(s)
            if k == 0:
                return
            for i in range(len(s) - 1):
                for j in range(i + 1, len(s)):
                    if s[i] < s[j]:
                        s = swap(s, i, j)
                        helper(s, k - 1)
                        s = swap(s, i, j)

        helper(A, B)
        return maxm


A = "254"
B = 1
A = "254"
B = 2

A = "473829"
B = 3
A = "7599"
B = 2
A = "129814999"
B = 4
test = Solution()
# print(test.solve(A, B))
# print(test.solve2(A, B))
print(test.solve4(A, B))
print(test.solve22(A, B))
