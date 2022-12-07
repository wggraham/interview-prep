class Solution:
    def getSum(self, a: int, b: int) -> int:
        r = 0
        mask = 1
        carry = 0

        for _ in range(32):
            bitA = a & mask
            bitB = b & mask
            r |= bitA ^ bitB if not (carry & mask) else ~(bitA ^ bitB) & mask
            carry = (bitA & bitB) | (carry & bitA) | (carry & bitB)
            carry <<= 1
            mask <<= 1
        return r


test = Solution()
print(test.getSum(20,30))
