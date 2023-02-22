class Solution:
    def numDecodings(self, A):
        if not A or A[0] == '0':
            return 0

        ways, s, n = [1, 1] + [0] * len(A), '00' + A, len(A) + 2
        for i in range(2, n):
            if 9 < int(s[i - 1: i + 1]) < 27:
                ways[i] += ways[i-2]
            if 0 < int(s[i]) < 10:
                ways[i] += ways[i-1]

        return ways[-1] % (10**9 + 7)

    def numDecodings2(self, A):
        if not A or A[0] == '0':
            return 0

        ways, A, n = [1, 1, 0], '00' + A, len(A) + 2
        for i in range(2, n):
            if 9 < int(A[i - 1: i + 1]) < 27:
                ways[2] += ways[0]
            if 0 < int(A[i]) < 10:
                ways[2] += ways[1]
            ways = ways[-2:] + [0]
        return ways[-2] % (10**9 + 7)

A = "11"
test = Solution()
print(test.numDecodings(A))
print(test.numDecodings2(A))
