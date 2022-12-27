class Solution:
    def grayCode(self, A):
        bits = [['0'], ['1']]
        for _ in range(A-1):
            bits = [['0'] + x for x in bits] + [['1'] + x for x in reversed(bits)]

        return [int(''.join(b), 2) for b in bits]


test = Solution()
print(test.grayCode(7))
