class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        oCount, cCount = 0, 0
        indices = set()

        for i, c in enumerate(s):
            if c == '(':
                oCount += 1
            if c == ')':
                cCount += 1
                if oCount - cCount < 0:
                    indices.add(i)
                    cCount -= 1

        for i in range(len(s) - 1, -1, -1):
            if oCount == cCount:
                break
            if s[i] == '(':
                indices.add(i)
                oCount -= 1
        return ''.join([c for i, c in enumerate(s) if i not in indices])

    def minRemoveToMakeValid2(self, s: str) -> str:
        l, r = 0, len(s) - 1
        indices = set()
        while l < r:
            while r >= l and s[r] != ')':
                if s[r] == '(':
                    indices.add(r)
                r -= 1
            while l <= r and s[l] != '(':
                if s[l] == ')':
                    indices.add(l)
                l += 1
            r -= 1
            l += 1

        return ''.join([c for i, c in enumerate(s) if i not in indices])

    def minRemoveToMakeValid3(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        return ''.join(c for i, c in enumerate(s) if i not in set(stack))


s = "lee(t(c)o)de)"
# s = "())()((("
# s = "((((("

test = Solution()
print(test.minRemoveToMakeValid(s))
print(test.minRemoveToMakeValid2(s))
print(test.minRemoveToMakeValid3(s))
