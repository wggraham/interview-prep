from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digitMap = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        s = [(1, [c]) for c in digitMap[digits[0]]]
        res = []

        while s:
            i, combo = s.pop()
            if i == len(digits):
                if len(combo) < len(digits):
                    continue
                res.append(''.join(combo))
            for j, d in enumerate(digits[i:], i):
                s.extend([(j + 1, combo + [c]) for c in digitMap[d]])

        return res


digits = "234"
test = Solution()
print(test.letterCombinations(digits))
