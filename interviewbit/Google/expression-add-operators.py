from typing import List


class Solution:
    # this doesn't concatenate multiple digits into 1 number
    def addOperators(self, num: str, target: int) -> List[str]:
        res, n = [], len(num)

        def tryOps(i, p, total, prev):
            if total > target:
                return
            if i == n:
                if total == target:
                    res.append(p)
                return
            if total < 0:
                tryOps(i + 1, p + ['*'] + [num[i]], prev - int(num[i-1]) * int(num[i]), prev)
            else:
                tryOps(i + 1, p + ['*'] + [num[i]], prev + int(num[i - 1]) * int(num[i]), prev)
            tryOps(i + 1, p + ['+'] + [num[i]], total + int(num[i]), total)
            tryOps(i + 1, p + ['-'] + [num[i]], total - int(num[i]), total)

        tryOps(1, [num[0]], int(num[0]), 0)
        return [''.join(s) for s in res]


num = "123"
target = 6
num = "232"
target = 8
# num = "3456237490"
# target = 9191
test = Solution()
print(test.addOperators(num, target))
