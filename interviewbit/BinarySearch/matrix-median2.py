import heapq
from heapq import heapify, heapreplace, heappop


class Solution:
    def findMedian(self, A):
        n, m = len(A) * len(A[0]), len(A[0])
        h = [(x[0], i, 0) for i, x in enumerate(A)]
        heapify(h)
        for _ in range(n // 2):
            if h[0][2] + 1 == m:
                heappop(h)
            else:
                heapreplace(h, (A[h[0][1]][h[0][2] + 1], h[0][1], h[0][2] + 1))

        return heappop(h)[0]

    # same cheat flattening list, then O(n*mlog n*m) sort, but uses extra memory
    def findMedian1(self, A):

        temp = []

        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                temp.append(A[i][j])

        temp.sort()

        return temp[len(temp) // 2]

        # l = 0
        # r = 1000*1000*1000
        # req = len(A) * len(A[0])
        # assert(req % 2);
        # while(r - l > 1):
        #     mid = l + (r - l) / 2
        #     cnt = 0
        #     for i in A:
        #         #using upper bound in a sorted array to count number of elements smaller than mid
        #         low = 0
        #         p = bisect.bisect_right(i, mid)
        #         cnt += p
        #     if cnt >= (req/2 +1):
        #         r = mid
        #     else:
        #         l = mid
        # return r

    # cheat by flattening to 1 list, still O(n log n)
    def findMedian2(self, A):
        A = [item for sublist in A for item in sublist]
        A.sort()
        # print(A)

        mid = (0 + len(A)) // 2

        return A[mid]

    # uses extra memory
    def findMedian3(self, A):
        m, n = len(A), len(A[0])
        A2 = []
        for i in range(m):
            A2 += A[0]
            del A[0]

        heapq.heapify(A2)

        for i in range((m * n) // 2 + 1):
            median = heapq.heappop(A2)
        return median


A = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]
A = [
  [2],
  [1],
  [4],
  [1],
  [2],
  [2],
  [5]
]
test = Solution()
print(test.findMedian(A))
