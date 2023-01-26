class Solution:
    # this doesn't work
    def checkRecord(self, n: int) -> int:
        binomial = [1, 2, 1]
        for i in range(3, n + 1):
            binomial[-2:] = [i, sum(binomial[-2:])]

        return (1 + n + binomial[-1]) * (n) % (10 ** 9 + 7)

    # use state machine representation
    def checkRecord2(self, n: int) -> int:
        s1 = s2 = s3 = s4 = s5 = 0
        s0 = 1
        for _ in range(n):
            temp_s0 = (s0 + s1 + s2) % 1000000007
            temp_s1 = s0
            temp_s2 = s1
            temp_s3 = (s0 + s1 + s2 + s3 + s4 + s5) % 1000000007
            temp_s4 = s3
            temp_s5 = s4
            s0, s1, s2, s3, s4, s5 = temp_s0, temp_s1, temp_s2, temp_s3, temp_s4, temp_s5

        return (s0 + s1 + s2 + s3 + s4 + s5) % 1000000007

    # use state machine representation
    def checkRecord3(self, n: int) -> int:
        s1 = s2 = s3 = s4 = s5 = 0
        s0 = 1
        for _ in range(n):
            s0, s1, s2, s3, s4, s5 = (s0 + s1 + s2) % 1000000007, s0, s1, \
                                     (s0 + s1 + s2 + s3 + s4 + s5) % 1000000007, s3, s4

        return (s0 + s1 + s2 + s3 + s4 + s5) % 1000000007

    # use state machine representation
    def checkRecord4(self, n: int) -> int:
        s0, s1, s2, s3, s4, s5, M = 1, 0, 0, 0, 0, 0, 1000000007
        for _ in range(n + 1):
            s0, s1, s2, s3, s4, s5 = (s0 + s1 + s2) % M, s0, s1, (
                        s0 + s1 + s2 + s3 + s4 + s5) % M, s3, s4

        return s3


n = 10
test = Solution()
print(test.checkRecord2(n))
print(test.checkRecord3(n))
print(test.checkRecord4(n))
