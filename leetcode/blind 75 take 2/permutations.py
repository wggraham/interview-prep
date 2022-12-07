import time
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_perms(a, p):
            if not a:
                res.append(p)
            for i in range(len(a)):
                get_perms(a[:i] + a[i + 1:], p + [a[i]])

        res = []
        get_perms(nums, [])
        return res

    # def permuteIterative(self, nums: List[int]) -> List[List[int]]:
    #     dp = [[nums[0]]]
    #     for i, v in enumerate(nums[1:], 1):
    #         t = []
    #         for p in dp:
    #             for j in range(i + 1):
    #                 t.append(p[:j] + [v] + p[j:])
    #         dp = t
    #     return dp

    def permuteIterative(self, nums: List[int]) -> List[List[int]]:
        dp = [[nums[0]]]
        for i, v in enumerate(nums[1:], 1):
            dp = [p[:j] + [v] + p[j:] for p in dp for j in range(i + 1)]
        return dp

    def permuteIterative2(self, nums: List[int]) -> List[List[int]]:
        dp = [[nums[0]]]
        for i, v in enumerate(nums[1:], 1):
            for k in range(len(dp)):
                # for j in range(1, i + 1):
                #     dp.append(dp[k][:j] + [v] + dp[k][j:])
                dp += [dp[k][:j] + [v] + dp[k][j:] for j in range(1, i + 1)]
                dp[k] = [v] + dp[k]
        return dp
    def permuteIterative3(self, nums: List[int]) -> List[List[int]]:
        dp = [[nums[0]]]
        for i, v in enumerate(nums[1:], 1):
            for k in range(len(dp)):
                for j in range(1, i + 1):
                    dp.append(dp[k][:j] + [v] + dp[k][j:])
                #dp += [dp[k][:j] + [v] + dp[k][j:] for j in range(1, i + 1)]
                dp[k] = [v] + dp[k]
        return dp

nums = [1, 2, 3]
test = Solution()
print(test.permuteIterative(nums))
for i in range(10, 11):
    t0 = time.time()
    test.permuteIterative3([j for j in range(1, i + 1)])
    t1 = time.time()
    test.permuteIterative([j for j in range(1, i + 1)])
    t2 = time.time()
    test.permuteIterative2([j for j in range(1, i + 1)])
    t3 = time.time()
    # print(x)
    # print(y)
    print("recursive: ", t1 - t0)
    print("iterative: ", t2 - t1)
    print("iterativeImproved: ", t3 - t2)
