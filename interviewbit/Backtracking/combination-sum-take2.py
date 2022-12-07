class Solution:
    def combinationSum(self, candidates, target):
        def gen_combos(nums, combo, total):
            if total < 0:
                return
            if total == 0:
                res.append(combo)
                return
            i = 0
            while nums and total >= 0:
                gen_combos(nums[1:], combo + [nums[0]] * i, total)
                total -= nums[0]
                i += 1

        candidates, res = sorted(list(set(candidates))), []
        gen_combos(candidates, [], target)
        return res[::-1]


nums = [1, 2, 3, 6, 7]
target = 7
test = Solution()
print(test.combinationSum(nums, target))
