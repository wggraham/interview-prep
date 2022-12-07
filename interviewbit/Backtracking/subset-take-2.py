class Solution:
    def subsets(self, nums):

        nums.sort()
        res = []

        def gen_subsets(nums, sub):
            res.append(sub)
            for i, v in enumerate(nums):
                gen_subsets(nums[i+1:], sub + [v])
        gen_subsets(nums, [])
        return res


nums = [1,2,3]
test = Solution()
print(test.subsets(nums))
