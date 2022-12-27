class Solution:
    def myPow(self, x: float, n: int) -> float:
        x, n = (1 / x, -n) if n < 0 else (x, n)
        ans = 1
        for _ in range(n):
            ans *= x
        return ans

    def myPowRecursive(self, x: float, n: int) -> float:
        def fast_pow(x, n):
            if not n: return 1.0
            half = fast_pow(x, n // 2)
            return half * half * x if n % 2 else half * half

        x, n = (1 / x, -n) if n < 0 else (x, n)
        return fast_pow(x, n)

    def myPowRecursive2(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    def myPowIterative(self, x: float, n: int) -> float:
        x, n = (1 / x, -n) if n < 0 else (x, n)
        ans, prod = 1, x
        while n:
            ans *= prod if n % 2 else 1
            prod *= prod
            n //= 2
        return ans

    def myPowIterative2(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


x = 2.00000
n = 10
test = Solution()
print(test.myPow(x, n))
print(test.myPowRecursive(x, n))
print(test.myPowIterative(x, n))
