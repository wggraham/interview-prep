class Solution:
    def subsetsWithDup(self, A):
        def gen_subsets(nums, sub):
            if sub in res: return
            res.add(sub)

            for i, v in enumerate(nums):
                gen_subsets(nums[i + 1:], sub + (v,))

        res = set()
        gen_subsets(sorted(A), ())
        return sorted([list(x) for x in res])


nums = [1, 2, 2]
test = Solution()
print(test.subsetsWithDup(nums))
