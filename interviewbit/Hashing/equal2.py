class Solution:
    def equal(self, nums):
        sums, n, res = {}, len(nums), []
        for i in range(n):
            for j in range(i + 1, n):
                total = nums[i] + nums[j]
                if total not in sums:
                    sums[total] = [i, j]
                elif i in sums[total] or j in sums[total]:
                    continue
                elif i > sums[total][0]:
                    sub = sums[total] + [i, j]
                    res = sub if not res or res > sub else res
        return res


nu = [3, 4, 7, 1, 2, 9, 8]
nu = [1, 1, 1, 1, 1]
# nu = [1, 3, 3, 3, 3, 2, 2]
nu = [9, 5, 4, 9, 3, 6, 8, 7, 1, 2, 8, 7, 2, 9, 7, 1, 3, 9, 7, 8, 1, 0, 5, 5]

test = Solution()
print(test.equal(nu))
