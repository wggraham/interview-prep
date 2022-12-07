from typing import List
from collections import defaultdict, deque
from copy import copy

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(set)
        p = defaultdict(set)
        for child, parent in prerequisites:
            if parent in p[child]:
                return False
            d[child].add(parent)
            p[parent].add(child)

        seen = set([x for x in range(numCourses)]).difference(d.keys())
        s = deque([(v, copy(seen)) for v in seen])
        while s:
            v, seen = s.popleft()
            if len(seen) == numCourses:
                return True
            for v in p[v]:
                if v in seen or not seen.issuperset(d[v]):
                    continue
                seen.add(v)
                s.append((v, seen))
        return False


a = 3
b = [[3,2],[1,2],[2,0]]
# a = 4
# b = [[0,1],[0,2],[1,3],[3,0]]
# numCourses = 5
# prerequisites = [[1,4],[2,4],[3,1],[3,2]]
# a = 2
# b = [[1,0]]
test = Solution()
print(test.canFinish(a, b))
