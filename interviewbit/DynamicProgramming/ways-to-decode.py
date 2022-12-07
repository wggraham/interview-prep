class Solution:
    def numDecodings(self, s):
        if not s or int(s[0]) == 0:
            return 0

        s = "00" + s
        ways = [0] * (len(s))
        ways[0] = ways[1] = 1

        for i in range(2, len(s)):
            if 9 < int(s[i-1: i+1]) < 27:
                ways[i] += ways[i-2]
            if 0 < int(s[i]) < 10:
                ways[i] += ways[i-1]

        return ways[-1]


test = Solution()
a = "1111"
print(test.numDecodings(a))
