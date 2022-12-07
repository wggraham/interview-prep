from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        res = []

        s = [(target, 0, [])]
        while s:
            total, i, t = s.pop()
            if total < 0:
                continue
            if total == 0:
                res.append(t)
            for j, v in enumerate(candidates[i:], i):
                temp = []
                newTotal = total
                while newTotal > 0:
                    newTotal -= v
                    temp.append(v)
                    s.append((newTotal, j+1, t + temp))
        return res


candidates = [2,3,6,7]
target = 7
candidates = [2,3,5]
target = 8
candidates = [2]
target = 1

test = Solution()
print(test.combinationSum(candidates, target))
