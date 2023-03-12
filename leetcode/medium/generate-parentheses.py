from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        prefixes = [("", 0, 0)]
        for _ in range(n * 2):
            temp = []
            for s, o_count, c_count in prefixes:
                temp += [(s + "(", o_count + 1, c_count)] if o_count < n else []
                temp += [(s + ")", o_count, c_count + 1)] if c_count < o_count else []
            prefixes = temp

        return [s for s, _, _ in prefixes]


test = Solution()
print(test.generateParenthesis(3))
