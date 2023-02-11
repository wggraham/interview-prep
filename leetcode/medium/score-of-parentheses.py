class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = count = 0
        for i, c in enumerate(s):
            if c == '(':
                count += 1
                continue

            count -= 1
            if s[i - 1] == '(':
                # score += 2 ** count
                score += 1 << count
        return score

    def scoreOfParentheses2(self, s: str) -> int:
        st = [0]
        for c in s:
            if c == '(':
                st += [0]
                continue

            v = st.pop()
            st[-1] += max(2 * v, 1)

        return st[-1]


s = "(()(()))"

test = Solution()
print(test.scoreOfParentheses(s))
print(test.scoreOfParentheses2(s))
