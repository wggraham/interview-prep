from copy import copy


class Solution:
    def __init__(self):
        self.keyMap = {
            "0": "0",
            "1": "1",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, A):

        if not A: return []

        res = list(self.keyMap[A[0]])
        for d in A[1:]:
            res2 = []
            for p in res:
                temp = [p + c for c in self.keyMap[d]]
                res2.extend(temp)
            res = res2

        return res


a = "23"
test = Solution()
print(test.letterCombinations(a))
