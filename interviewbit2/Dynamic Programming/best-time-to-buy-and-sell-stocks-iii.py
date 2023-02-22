from sys import maxsize


class Solution:
    def maxProfit(self, A):
        s0, s1, s2, s3 = maxsize, -maxsize, -maxsize, -maxsize
        for i, p in enumerate(A):
            s0 = min(s0, p)
            s1 = max(s1, p - s0)
            s2 = max(s2, s1 - p)
            s3 = max(s3, s2 + p)

        return max(s1, s3)

    def maxProfit2(self, price):
        s0, s1, s2, s3 = maxsize, -maxsize, -maxsize, -maxsize
        for p in price:
            s0, s1, s2, s3 = min(s0, p), max(s1, p - s0), max(s2, s1 - p), max(s3, s2 + p)

        return max(s1, s3) if max(s1, s3) > 0 else 0


A = [7, 2, 4, 8, 7]
# A = [1, 2, 1, 2]

test = Solution()
print(test.maxProfit(A))
print(test.maxProfit2(A))
