from math import factorial


class Solution:
    def getPermutation(self, A, k):

        def gen_perms(nums, perm):
            nonlocal k
            if not nums:
                k -= 1
                return perm

            for i, v in enumerate(nums):
                ans = gen_perms(nums[:i] + nums[i + 1:], perm + [v])
                if k <= 0:
                    break
            return ans

        return ''.join(str(x) for x in gen_perms([x for x in range(1, A + 1)], []))

    def getPermutation2(self, n, k):
        nums, perm = list(range(1, n + 1)), []
        k -= 1
        for v in reversed(range(n)):
            i, k = divmod(k, factorial(v))
            perm += [nums[i]]
            nums.remove(nums[i])

        return ''.join(str(x) for x in perm)


n = 100
k = 10000000
n = 3
k = 4
n = 1
k = 1
test = Solution()
print(test.getPermutation(n, k))
print(test.getPermutation2(n, k))
