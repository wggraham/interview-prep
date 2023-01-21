class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans, prev = 0, roman_map[s[0]]
        for c in s:
            val = roman_map[c]
            if val > prev:
                ans -= prev << 1

            ans += val
            prev = val
        return ans

    def romanToInt2(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = prev = 0
        for c in reversed(s):
            val = roman_map[c]
            if val < prev:
                ans -= val
            else:
                ans += val
            prev = val
        return ans

    def romanToInt3(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = roman_map[s[0]]
        for i, c in enumerate(s[1:], 1):
            if roman_map[c] > roman_map[s[i-1]]:
                ans += roman_map[c] - roman_map[s[i-1]] * 2
            else:
                ans += roman_map[c]
        return ans

    def romanToInt4(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans, prev = 0, roman_map[s[0]]
        for c in s:
            val = roman_map[c]
            if val > prev:
                ans += val - (prev << 1)
            else:
                ans += val
            prev = val
        return ans


s = "MCMXCIV"
# s = "LVIII"
test = Solution()
print(test.romanToInt(s))
print(test.romanToInt2(s))
print(test.romanToInt4(s))
