from heapq import heapify, heappop, heappush
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        h = [(A[0] + A[1], 0, 1), (A[-1] + A[-2], n-2, n-1)]
        for i in range(1, len(A)-1):
            h.append((A[i] + A[i + 1], i, i + 1))
            h.append((A[i - 1] + A[i])
        heapify(h)

