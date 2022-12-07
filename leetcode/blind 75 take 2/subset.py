from typing import List


class Solution:
    # this way works for sets only
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def get_subsets(i, p):
            res.append(p)

            for j in range(i, n):
                get_subsets(j + 1, p + [nums[j]])

        get_subsets(0, [])
        return res

    # this way works for sets only
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for num in nums:
            res += [p + [num] for p in res]
        return res

    # this way works with duplicates
    def subsets4(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums += [0]
        res = [[]]
        for i, num in enumerate(nums[:-1]):
            t = []
            if num == nums[i-1]:
                j = -1
                while res[j] and res[j][-1] == num:
                    t.append(res[j] + [num])
                    j -= 1
                res += reversed(t)
            else:
                for p in res:
                    t.append(p + [num])
                res += t
        return res




nums = [1,1,2,2,3,3]
test = Solution()
#print(test.subsets(nums))
# print(test.subsets(nums))
# print(test.subsets3(nums))
print(test.subsets4(nums))
