class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def count_longest(t, paren):
            l, r, longest = 0, 0, 0
            for c in t:
                l, r = ((c == paren), (c != paren)) if r > l else (l + (c == paren), r + (c != paren))
                longest = max(longest, r * 2) if l == r else longest

            return longest

        return max(count_longest(s, '('), count_longest(s[::-1], ')'))


s = "()(()"
# s = ")()())"
# s = "()"
# s = "()()()"
# s = ")()(((())))("
# s = "(((())))"
# s = "))))((()(("
# s = "))))())()()(()"
s = ")()())()()("
test = Solution()
print(test.longestValidParentheses(s))
