class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a if not b else self.getSum(a ^ b, (a & b) << 1)

    def getSum2(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)

    def getSum3(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign

    def getSum4(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
        # sum of two positive integers x + y
        # where x > y

        # TODO
        else:
        # difference of two integers x - y
        # where x > y

        # TODO

        return x * sign

    
a = -1
b = -4
test = Solution()
print(test.getSum(a, b))
print(test.getSum2(a, b))
