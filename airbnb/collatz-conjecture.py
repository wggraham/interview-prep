# Given an integer n, output the max steps of transform number in [1, n] into 1.
class Solution:
    def getSteps(self, num):
        if num < 1:
            return 0
        steps = {1: 0}

        def count(n):
            if n in steps:
                return steps[n]

            steps[n] = count(3 * n + 1) + 1 if n % 2 else count(n // 2) + 1
            return steps[n]

        res = 0
        for v in range(1, num + 1):
            res = max(res, count(v))
        return res + 1


test = Solution()
print(test.getSteps(101))
