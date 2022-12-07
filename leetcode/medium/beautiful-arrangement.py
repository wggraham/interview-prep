from math import ceil, sqrt


class Solution:
    @staticmethod
    def __getDivisors(n):
        root = ceil(sqrt(n))
        divisors = []
        for i in range(1, min(n//2, root)+1):
            if not n % i:
                divisors.append(i)
        return divisors

    # iterate over partial sums swapping new i for divisible value, in divisible columns
    @staticmethod
    def __getFinal(arrs, n):
        final = []
        seen = set()
        divisors = Solution.__getDivisors(n)
        fixed = [p + [n] for p in arrs]

        for a in arrs:
            for j in divisors:
                if n % a[j-1]:
                    continue

                x = tuple(a[:j-1] + [n] + a[j-1:])
                if x not in seen:
                    seen.add(x)
                    final.append(a[:j-1] + [n] + a[j:] + [a[j-1]])
        return fixed + final

    def countArrangement(self, n: int) -> int:
        final = [[1]]
        for i in range(2, n + 1):
            final = Solution.__getFinal(final, i)

        return len(final)


test = Solution()
print(test.countArrangement(6))

