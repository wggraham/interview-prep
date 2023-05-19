class Solution:
    def maxSpecialProduct(self, A):
        def set_special(i, nums, s, special):
            while s and nums[s[-1]] <= nums[i]:
                s.pop()
            special[i] *= s[-1] if s else 0
            s.append(i)

        s, res = [], [1] * len(A)
        for i in range(len(A)):
            set_special(i, A, s, res)
        s = []
        for i in reversed(range(len(A))):
            set_special(i, A, s, res)

        return max(res) % ((10**9) + 7)

    def maxSpecialProduct2(self, A):
        mx, res = (0, -1), [-1] * len(A)
        for i, v in enumerate(A):
            mx = max(mx, (v, i))
            res[i] = mx[1] if mx[0] != v else 0

        ans, mx = 0, (0, -1)
        for i in reversed(range(len(A))):
            mx = max(mx, (A[i], i))
            if A[i] < mx[0] and res[i] != 0:
                ans = max(ans, mx[1] * res[i])

        return ans % ((10**9) + 7)


A = [1, 4, 3, 4]
test = Solution()
print(test.maxSpecialProduct(A))
print(test.maxSpecialProduct2(A))


