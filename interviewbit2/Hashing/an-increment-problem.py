from bisect import bisect_left
from collections import defaultdict, deque


class Solution:
    def solve(self, A):
        stream, loc = [], defaultdict(deque)
        for i, v in enumerate(A):
            if v in loc:
                j = loc[v].popleft()
                stream[j] += 1
                if stream[j] in loc:
                    k = bisect_left(loc[stream[j]], j)
                    loc[stream[j]].insert(k, j)
                else:
                    loc[stream[j]].append(j)
                if not loc[v]:
                    del loc[v]
            loc[v].append(len(stream))
            stream.append(v)
        return stream


A = [3, 1, 3, 2]
A = [1, 1, 2, 2]
test = Solution()
print(test.solve(A))
