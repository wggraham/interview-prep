from collections import defaultdict
from sys import maxsize
from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        rMin, rMax = min([start for (start, _) in paint]), max([end for (_, end) in paint])

        rng = set([x for x in range(rMin, rMax)])
        res = []
        for (start, end) in paint:
            total = 0
            for x in range(start, end):
                if x not in rng: continue
                rng.remove(x)
                total += 1

            res.append(total)
        return res

    def amountPainted3(self, paint: List[List[int]]) -> List[int]:
        records, rMin, rMax, rng, res = defaultdict(int), maxsize, 0, set(), [0] * len(paint)

        for i, (start, end) in enumerate(paint):
            if (start, end) in records: continue
            records[(start, end)] = i
            rMin, rMax = min(rMin, start), max(rMax, end)

        for (start, end), i in records.items():
            total = 0
            for x in range(start, end):
                if x in rng: continue
                rng.add(x)
                total += 1

            res[i] = total
        return res

    # def amountPainted2(self, paint: List[List[int]]) -> List[int]:
    #     rMin, rMax = min([start for (start, _) in paint]), max([end for (_, end) in paint])
    #     # records = [(start, end, i) for i, (start, end) in enumerate(paint)]
    #     # records.sort(key=lambda x: (x[0], -x[1], x[2]))
    #
    #     rng = set([x for x in range(rMin, rMax)])
    #     res = [0] * len(paint)
    #     j  = 0
    #     for i in range(rMax+1):
    #         while j < len(paint) and records[j][0] == i:
    #             i, j,


paint = [[1, 4], [5, 8], [4, 7]]
test = Solution()
# print(test.amountPainted(paint))
print(test.amountPainted3(paint))