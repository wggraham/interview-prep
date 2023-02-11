from heapq import heapify, heappop, heappush
from sys import maxsize
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res, s, arr = 0, [0], [-maxsize] + arr + [-maxsize + 1],
        for i, v in enumerate(arr[1:], 1):
            while s and arr[s[-1]] >= v:
                mid = s.pop()
                left = s[-1]
                count = (mid - left) * (i - mid)
                res += count * arr[mid]

            s.append(i)

        return res % (10 ** 9 + 7)

    def sumSubarrayMins2(self, arr: List[int]) -> int:
        res, s, MOD = 0, [], 10 ** 9 + 7

        for i in range(len(arr) + 1):
            while s and (i == len(arr) or arr[s[-1]] >= arr[i]):
                mid = s.pop()
                left = -1 if not s else s[-1]
                right = i

                count = (mid - left) * (right - mid)
                res += count * arr[mid]

            s.append(i)

        return res % MOD

    # Monotonic Stack + Dynamic Programming
    def sumSubarrayMins3(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # monotonic increasing stack
        stack = []

        # make a dp array of the same size as the input array
        dp = [0] * len(arr)

        # populate monotonically increasing stack
        for i in range(len(arr)):
            # before pushing an element, make sure all
            # larger and equal elements in the stack are
            # removed
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # calculate the sum of minimums of all subarrays
            # ending at index i
            if stack:
                previousSmaller = stack[-1]
                dp[i] = dp[previousSmaller] + (i - previousSmaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            stack.append(i)

        # add all the elements of dp to get the answer
        return sum(dp) % MOD


arr = [3, 1, 2, 4]
test = Solution()
print(test.sumSubarrayMins(arr))
print(test.sumSubarrayMins2(arr))
print(test.sumSubarrayMins3(arr))