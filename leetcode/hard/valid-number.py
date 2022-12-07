from copy import copy
class Solution:
    def isNumber(self, s: str) -> bool:
        valid = {'+', '-', 'e', 'E', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        signs = {'+', '-'}

        v = copy(valid)
        for i, c in enumerate(s):
            if c not in v:
                return False
            if c in digits:
                v = copy(valid)
            elif c == '.':
                v = v.difference(signs)
                v.remove('.')
            elif c == 'e' or c == 'E':
                if i and (s[i-1] != '.' or s[i-1] not in digits):
                    return False
                v.remove('e')
                v.remove('E')
            else:
                v = v.difference(signs)

        return True if 'e' in v or 'E' in v else False


test = Solution()
valid = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
invalid = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for s in valid:
    print("Want: True Got: ", test.isNumber(s))

for s in invalid:
    print("Want: False Got: ", test.isNumber(s))
