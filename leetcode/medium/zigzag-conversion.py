class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        r, inc, res = 0, True, [[] for _ in range(numRows)]
        res[0].append(s[0])
        for c in s[1:]:
            inc = not inc if (r == 0 and not inc) or (r == numRows - 1 and inc) else inc
            r += 1 if inc else -1
            res[r].append(c)
        return ''.join(''.join(x) for x in res)


s = "PAYPALISHIRING"
numRows = 4
s = "ABC"
numRows = 1
test = Solution()
print(test.convert(s, numRows))
