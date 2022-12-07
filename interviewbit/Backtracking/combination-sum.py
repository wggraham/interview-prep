import time

class Solution:
    def combinationSum(self, A, B):
        allCombos = []

        def combos(nums, target, combo):
            if target < 0: return
            if target == 0:
                allCombos.append(combo)

            for i, val in enumerate(nums):
                combos(nums[i:], target - val, combo + [val])

        combos(sorted(set(A)), B, [])
        return allCombos

    def combinationSum2(self, A, B):
        def combos(nums, target, combo):
            if target < 0: return
            if target == 0:
                return [combo]
            c = []
            for i, val in enumerate(nums):
                x = combos(nums[i:], target - val, combo + [val])
                if x:
                    c.extend(x)
            return c
        return combos(sorted(set(A)), B, [])

a = [2, 3, 6, 7]
b = 7
a = [ 8, 10, 6, 11, 1, 16, 8 ]
b = 28
test = Solution()
print(test.combinationSum(a, b))
print(test.combinationSum2(a, b))

test = Solution()
t0 = time.time()
test.combinationSum(A, B)
t1 = time.time()
test.combinationSum2(A, B)
t2 = time.time()

print(t1-t0)
print(t2-t1)
