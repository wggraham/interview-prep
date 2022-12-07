from collections import defaultdict
from sys import maxsize
from typing import List

from sortedcontainers import SortedList


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
    #     starts, ends, rMin, rMax, n = [], [], maxsize, 0, len(paint)
    #
    #     for i, start, end in enumerate(paint):
    #         starts.append((start, i))
    #         ends.append((end, i))
    #     starts.sort(reverse=True)
    #     ends.sort(reverse=True)
    #
    #     res = [0] * n
    #     indices = SortedList()
    #     for i in range(n):
    #         start, s = starts.pop()
    #         end, e = ends.pop()
    #         if indices:
    #             res[indices[0]] +=
    #
    #         indices.add(s)
    #         indices.remove(e)

    def amountPainted4(self, paint: List[List[int]]) -> List[int]:
        records, rMin, rMax, n = [], maxsize, 0, len(paint)

        for i, (start, end) in enumerate(paint):
            records.append((start, i, False))
            records.append((end, i, True))
        records.sort()

        res = [0] * n
        indices = SortedList()
        end = records[0][0]
        for loc, index, isEnd in records:
            if indices:
                res[indices[0]] += loc - end
            end = loc

            if isEnd:
                indices.remove(index)
            else:
                indices.add(index)

        return res


paint = [[1, 4], [5, 8], [4, 7]]
test = Solution()
print(test.amountPainted(paint))
print(test.amountPainted4(paint))
