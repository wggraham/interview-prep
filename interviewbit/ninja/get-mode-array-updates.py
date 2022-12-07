from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def getMode(self, A, B):
        counts = Counter(A)
        modes = []
        h = [(-count, val) for val, count in counts.items()]
        heapify(h)
        for i, v in B:
            if A[i-1] != v:
                counts[v] += 1
                counts[A[i-1]] -= 1
                heappush(h, (-counts[v], v))
                heappush(h, (-counts[A[i-1]], A[i-1]))
                A[i-1] = v

            while counts[h[0][1]] != -h[0][0]:
                heappop(h)
            modes.append(h[0][1])
        return modes


A = [2, 2, 2, 3, 3]
Updates = [[1, 3],
           [5, 4],
           [2, 4]]
# A = [ 3, 2, 1, 1, 3 ]
# Updates = [
#   [2, 2],
#   [3, 3],
#   [3, 3],
#   [2, 1],
#   [4, 3]
# ]
test = Solution()
print(test.getMode(A, Updates))

