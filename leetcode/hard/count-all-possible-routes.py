from typing import List
from collections import defaultdict

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if not locations or len(locations) < 1: return 0

        p = defaultdict()
        def countR(i, f):
            count = 0
            if i == finish:
                if not f:
                    return 1
                count += 1
            for j, _ in enumerate(locations):
                if i == j:
                    continue
                if f - abs(locations[i] - locations[j]) - abs(locations[j] - locations[finish]) >= 0:
                    if (j, f - abs(locations[i] - locations[j])) not in p:
                        p[(j, f - abs(locations[i] - locations[j]))] = countR(j, f - abs(locations[i] - locations[j]))
                    count += p[(j, f - abs(locations[i] - locations[j]))]
            return count

        return countR(start, fuel)


l = [1,2,3]
s = 0
fin = 2
fuel = 40
test = Solution()
print(test.countRoutes(l, s, fin, fuel))
