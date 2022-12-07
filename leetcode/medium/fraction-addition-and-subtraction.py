import math
from fractions import Fraction


class Solution:
    @staticmethod
    def getNomDenom(s, i, j):
        k = i
        while s[k] != '/':
            k += 1
        return [int(s[i:k]), int(s[k:1:j])]

    @staticmethod
    def lcm(r):
        def getLcm(a, b):
            a, b = [a, b] if a >= b else [b, a]
            ao = a
            i = 2
            while b % a:
                a = ao * i
                i += 1
            return a

        a = r[0].denominator
        for i, f in enumerate(r[1:]):
            b = f.denominator
            x = getLcm(a, b)
            r[i] *= x / a

    def fractionAddition(self, s):
        n = len(s)
        i, j = n - 1, n - 1
        res = []
        while j >= 0:
            if s[j] == '+' or s[j] == '-':
                res.append(Fraction(s[j:i+1]))
                i, j = j - 1, j - 1
            j -= 1

        # check last group
        if i > 0:
            res.append(Fraction(s[:i+1]))

        r = sum(res)
        sign = '' if r.numerator >= 0 else '-'
        return "{sign}{num}/{denom}".format(sign=sign, num=str(r.numerator), denom=str(r.denominator))


t = "-1/2+1/2"
t ="-1/2+1/2+1/3"
t = "5/3+1/3"
test = Solution()
print(test.fractionAddition(t))
