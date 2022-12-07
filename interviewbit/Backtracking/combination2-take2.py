class Solution:
    def combinationSum(self, candidates, target):
        def gen_combos(nums, combo, total):
            if total < 0:
                return
            if total == 0:
                t = tuple(combo)
                if t not in seen:
                    res.append(combo)
                    seen.add(t)
                return

            for i, v in enumerate(nums):
                gen_combos(nums[i + 1:], combo + [v], total - v)

        candidates.sort()
        res, seen = [], set()
        gen_combos(candidates, [], target)
        return res


nums = [10, 1, 2, 7, 6, 1, 5]
target = 8
test = Solution()
print(test.combinationSum(nums, target))
