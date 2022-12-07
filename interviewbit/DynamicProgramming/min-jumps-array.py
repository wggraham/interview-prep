from collections import deque


class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n == 1:
            return 0
        s = deque([(0, 0)])
        seen = {0}
        while s:
            i, jumps = s.popleft()

            for j in reversed(range(i + 1, min(i + 1 + A[i], n))):
                if j == n - 1:
                    return jumps + 1
                if j not in seen:
                    seen.add(j)
                    s.append((j, jumps + 1))
        return -1

A = [2, 3, 1, 1, 4]
test = Solution()
print(test.jump(A))
