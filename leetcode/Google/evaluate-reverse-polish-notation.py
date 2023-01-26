from operator import add, sub, truediv, mul
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s, ops = [], {'+': add, '-': sub, '/': truediv, '*': mul}
        for t in tokens:
            if t in ops:
                s[-2:] = [int(ops[t](s[-2], s[-1]))]
            else:
                s += [int(t)]

        return s[-1]


tokens = ["2", "1", "+", "3", "*"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens = ["4", "13", "5", "/", "+"]
test = Solution()
print(test.evalRPN(tokens))
