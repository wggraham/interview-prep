from functools import cmp_to_key


class Solution:
    # def largestNumber(self, A):
    #     A.sort(reverse=True, key=lambda x: list(str(x))[0])
    #     for c in string.digits:
    #         d = int(c)
    #         while
    #
    #
    #     return ''.join(sorted([str(v) for v in A], key=lambda x: x, reverse=True))

    def largestNumber(self, A):
        res = ''.join(sorted(map(str, A), key=cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1), reverse=True)).lstrip('0')
        return res if res else '0'


A = [3, 30, 34, 5, 9]
test = Solution()
print(test.largestNumber(A))
