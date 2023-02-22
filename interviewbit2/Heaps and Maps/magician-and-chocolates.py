from heapq import heapify, heapreplace


class Solution:
    def nchoc(self, A, B):
        h = [-v for v in B]
        heapify(h)
        ans = 0

        for _ in range(A):
            ans += -heapreplace(h, (-(-h[0] // 2)))

        return ans % (10 ** 9 + 7)


A = 5
B = [2, 4, 6, 8, 10]
test = Solution()
print(test.nchoc(A, B))
