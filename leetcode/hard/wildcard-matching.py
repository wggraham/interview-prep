class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) < 1:
            return p == s
        stack = [(len(s) - 1, len(p) - 1)]
        while stack:
            i, j = stack.pop()
            if i == -1:
                while j >= 0 and p[j] == '*':
                    j -= 1
                if j == -1:
                    return True
                continue
            if j == -1:
                continue
            if p[j] == '?' or s[i] == p[j]:
                stack.append((i - 1, j - 1))
            elif p[j] == '*':
                stack.extend([(i, j - 1) for i in range(i, -2, -1)])

        return False


s = "aa"
p = "a"
p = "*"
# s = "cb"
# p = "?a"
s = "adceb"
p = "*a*b"
# s = "aa"
# p = "aa"
s = "a"
p = ""
s = "abbbb"
p = "b**?"
s = "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab"
p = "*aabb***aa**a******aa*"
test = Solution()
print(test.isMatch(s, p))
