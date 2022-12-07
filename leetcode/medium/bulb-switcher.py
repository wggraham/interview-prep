class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n < 4:
            return 1
        a = [i % 2 for i in range(1, n + 1)]
        total = 1
        for i in range(3, n+1):
            for j in range(i, n+1, i):
                a[i-1] = 0 if a[i-1] else 1

            total += a[i-1]

        return total


n = 9
test = Solution()
print(test.bulbSwitch(n))
