from math import factorial


class Solution:
    def getPermutation(self, n, k):
        def gen_perm(nums, perm):
            nonlocal found, k
            if found: return
            if not nums:
                k -= 1
                if k == 0:
                    found = True
                    return ''.join(str(i) for i in perm)

            for i, v in enumerate(nums):
                ans = gen_perm(nums[:i] + nums[i + 1:], perm + [v])
                if ans:
                    return ans

        found = False
        return gen_perm([i for i in range(1, n + 1)], [])

    def getPermutation2(self, n, k):
        nums, perm, k = list(range(1, n + 1)), [], k - 1
        for i in range(n, 1, -1):
            j, k = divmod(k, factorial(n))
            perm += [nums[j]]
            nums.remove(nums[j])

        return ''.join(str(i) for i in perm)


n = 3
k = 4
A = 100
B = 10000000
test = Solution()
print(test.getPermutation2(A, B))
