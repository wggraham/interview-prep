from sortedcontainers import SortedSet
from typing import List


class Solution:
    def largestVariance(self, s: str) -> int:
        def maxSubArray(nums: List[int]):
            total = m_sum = 0
            seen = True
            for v in nums:
                total = max(v, total + v)
                seen = not seen if total == v else seen
                m_sum = max(m_sum, total) if seen and total != v else max(m_sum, total - 1)

            return m_sum

        st = SortedSet(s)
        n, m, res = len(s), len(st), 0

        for i, x in enumerate(st.__iter__()):
            for j, y in enumerate(st[i + 1:].__iter__(), i + 1):
                arr = []
                for k in range(n):
                    if s[k] not in (x, y):
                        continue
                    arr += [1] if s[k] == x else [-1]

                res = max(res, maxSubArray(arr), maxSubArray([-x for x in arr]))
        return res

    def largestVariance2(self, s: str) -> int:
        def maxSubArray(nums: List[int]):
            ans=-float('inf')
            runningSum=0
            seen=False
            for x in (nums):
                if x<0:
                    seen=True
                runningSum+=x
                if seen:
                    ans=max(ans,runningSum)
                else:
                    ans=max(ans,runningSum-1)
                if runningSum<0:
                    runningSum=0
                    seen=False
            return ans

        f = set()
        a = ''
        for x in s:
            if x not in f:
                a += x
                f.add(x)

        n = len(s)
        res = 0
        for j in range(len(a) - 1):
            for k in range(j + 1, len(a)):
                x = a[j]
                y = a[k]
                arr = []
                for i in range(n):
                    if s[i] != x and s[i] != y:
                        continue
                    elif s[i] == x:
                        arr.append(1)
                    else:
                        arr.append(-1)

                res = max(res, maxSubArray(arr), maxSubArray([-x for x in arr]))

        return res


s = "aababbb"
s = "aababbb"
# s = "abcde"
s = "lripaa"
test = Solution()
print(test.largestVariance(s))
print(test.largestVariance2(s))

