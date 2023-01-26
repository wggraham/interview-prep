from collections import Counter
from typing import List


class Solution:
    def __init__(self):
        self.n = None

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(x):
            while parent[x] != x:
                parent[x], x = parent[parent[x]], parent[x]
            return x

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            rank[root_x] = rank[root_y] = rank[root_x] + rank[root_y]
            parent[root_y] = root_x

            return rank[root_x] == n

        parent = {i: i for i in range(n)}
        rank = Counter(i for i in range(n))
        for time, a, b in sorted(logs):
            if union(a, b):
                return time

        return -1

    def earliestAcq2(self, logs: List[List[int]], n: int) -> int:
        def find(x):
            while parent[x] != x:
                parent[x], x = parent[parent[x]], parent[x]
            return x

        def union(x, y):
            nonlocal n
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                n -= 1
                parent[root_y] = root_x

        parent = {i: i for i in range(n)}
        n -= 1
        for time, a, b in sorted(logs):
            union(a, b)
            if not n:
                return time

        return -1


logs = [
    [20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
    [20190312, 1, 2], [20190322, 4, 5]
]
n = 6
test = Solution()
print(test.earliestAcq(logs, n))
print(test.earliestAcq2(logs, n))
