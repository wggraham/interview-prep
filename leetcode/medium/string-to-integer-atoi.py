from _testcapi import INT_MAX, INT_MIN


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        res, i = 0, 0
        while i < len(s) and s[i] == ' ':
            i += 1
        j = i
        if i < len(s) and (s[i] == '+' or s[i] == '-'): i += 1
        while i < len(s) and s[i] == '0': i += 1
        for d in s[i:]:
            if not d.isdigit():
                break
            res *= 10
            res += ord(d) - ord('0')
        res = -res if j < len(s) and s[j] == '-' else res
        res = INT_MAX if res > INT_MAX else res
        res = INT_MIN if res < INT_MIN else res
        return res

    def myAtoi2(self, s: str) -> int:
        res, s = 0, s.strip()
        for d in s[1:] if len(s) and s[0] in ['-', '+'] else s:
            if not d.isdigit(): break
            res = res * 10 + ord(d) - ord('0')
        res = max(INT_MIN, res * -1) if len(s) and s[0] == '-' else res
        return min(INT_MAX, res) if len(s) and s[0] != '-' else res


s = '   -42'
s = "-14193 with words"
test = Solution()
print(test.myAtoi(s))
print(test.myAtoi2(s))
